"""Strict structured RCA output and citation validation, independent of providers."""
import json
from dataclasses import dataclass
from daicp.contracts.models import Evidence


class RCAOutputError(ValueError):
    """Generated output violates the shape or references unavailable evidence."""


@dataclass(frozen=True)
class Hypothesis:
    """A model-generated hypothesis, not a verified causal finding."""

    explanation: str
    evidence_ids: tuple[str, ...]


@dataclass(frozen=True)
class RCAResult:
    """Validated answer plus the exact source evidence supplied to the model."""

    incident_id: str
    status: str
    hypotheses: tuple[Hypothesis, ...]
    uncertainty: tuple[str, ...]
    next_steps: tuple[str, ...]
    evidence: tuple[Evidence, ...]


class RCAOutputValidator:
    """Validate JSON shape and citation membership; this is not a truth verifier."""

    @staticmethod
    def json_schema() -> dict:
        nonempty = {"type": "string", "minLength": 1}
        return {
            "type": "object", "additionalProperties": False,
            "required": ["status", "hypotheses", "uncertainty", "next_steps"],
            "properties": {
                "status": {"type": "string", "enum": ["hypotheses", "abstained"]},
                "hypotheses": {"type": "array", "items": {
                    "type": "object", "additionalProperties": False,
                    "required": ["explanation", "evidence_ids"],
                    "properties": {"explanation": nonempty,
                        "evidence_ids": {"type": "array", "minItems": 1,
                                         "uniqueItems": True, "items": nonempty}}}},
                "uncertainty": {"type": "array", "minItems": 1, "items": nonempty},
                "next_steps": {"type": "array", "items": nonempty},
            },
        }

    @staticmethod
    def _strings(value, name: str, nonempty: bool = False) -> tuple[str, ...]:
        if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
            raise RCAOutputError(f"{name} must be an array of non-empty strings.")
        if nonempty and not value:
            raise RCAOutputError(f"{name} must not be empty.")
        return tuple(value)

    def parse(self, text: str, incident_id: str, evidence: tuple[Evidence, ...]) -> RCAResult:
        try:
            payload = json.loads(text)
        except (ValueError, TypeError) as exc:
            raise RCAOutputError("LLM response is not a JSON object.") from exc
        required = {"status", "hypotheses", "uncertainty", "next_steps"}
        if not isinstance(payload, dict) or set(payload) != required:
            raise RCAOutputError("Unexpected or missing RCA output fields.")
        if payload["status"] not in ("hypotheses", "abstained"):
            raise RCAOutputError("Invalid RCA status.")
        if not isinstance(payload["hypotheses"], list):
            raise RCAOutputError("hypotheses must be an array.")
        available = {item.evidence_id for item in evidence}
        hypotheses = []
        for item in payload["hypotheses"]:
            if not isinstance(item, dict) or set(item) != {"explanation", "evidence_ids"}:
                raise RCAOutputError("Invalid hypothesis fields.")
            if not isinstance(item["explanation"], str) or not item["explanation"].strip():
                raise RCAOutputError("A hypothesis explanation is required.")
            ids = self._strings(item["evidence_ids"], "evidence_ids", True)
            if len(ids) != len(set(ids)) or not set(ids) <= available:
                raise RCAOutputError("A hypothesis cites unknown or repeated evidence IDs.")
            hypotheses.append(Hypothesis(item["explanation"], ids))
        if bool(hypotheses) != (payload["status"] == "hypotheses"):
            raise RCAOutputError("RCA status contradicts the hypothesis list.")
        return RCAResult(incident_id, payload["status"], tuple(hypotheses),
            self._strings(payload["uncertainty"], "uncertainty", True),
            self._strings(payload["next_steps"], "next_steps"), evidence)
