"""Compose retrieval and provider generation into a bounded RCA operation."""
from daicp.contracts.models import Incident
from daicp.backend.llm.provider import LLMProvider
from daicp.backend.retrieval.service import RetrievalService
from .output_schema import RCAOutputValidator, RCAResult
from .prompt import RCAPromptBuilder


class RCAService:
    """Run one analysis; no agent loop, tool execution or evaluation-label access."""

    def __init__(self, retrieval: RetrievalService, provider: LLMProvider,
                 prompt_builder: RCAPromptBuilder | None = None) -> None:
        self.retrieval, self.provider = retrieval, provider
        self.prompt_builder = prompt_builder or RCAPromptBuilder()
        self.validator = RCAOutputValidator()

    def analyze(self, incident: Incident, query: str | None = None,
                top_k: int = 5, min_score: float = 0.25) -> RCAResult:
        query = query if query is not None else incident.summary + "\n" + "\n".join(
            item.text for item in incident.evidence)[:2000]
        retrieved = self.retrieval.search(query, top_k=top_k, min_score=min_score)
        by_id = {item.evidence_id: item for item in incident.evidence}
        for result in retrieved:
            item = result.evidence
            if item.evidence_id in by_id and by_id[item.evidence_id] != item:
                raise ValueError("Conflicting evidence with the same ID.")
            by_id[item.evidence_id] = item
        evidence = tuple(by_id.values())
        if not evidence:
            return RCAResult(incident.incident_id, "abstained", (),
                ("No incident observations or relevant knowledge were available.",),
                ("Collect operational observations and approved technical documentation.",), ())
        prompt = self.prompt_builder.build(incident, evidence)
        generated = self.provider.generate(prompt, self.prompt_builder.SYSTEM,
                                           self.validator.json_schema())
        return self.validator.parse(generated, incident.incident_id, evidence)
