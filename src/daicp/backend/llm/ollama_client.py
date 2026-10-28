"""Ollama HTTP adapter with bounded requests and structured JSON output."""
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from .provider import LLMProvider, LLMProviderError

model = "qwen3:8b"


class OllamaProvider(LLMProvider):
    """Use an already installed Ollama model; never download models implicitly."""

    def __init__(self, model: str = model, host: str = "http://localhost:11434",
                 timeout: float = 120, num_predict: int = 2048) -> None:
        parsed = urlparse(host)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Ollama host must be an HTTP(S) URL.")
        if not model.strip() or timeout <= 0 or num_predict < 1:
            raise ValueError("Model, positive timeout and token limit are required.")
        self.model, self.host = model, host.rstrip("/")
        self.timeout, self.num_predict = timeout, num_predict

    def _request(self, payload: dict) -> dict:
        request = Request(self.host + "/api/generate",
                          data=json.dumps(payload).encode("utf-8"),
                          headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urlopen(request, timeout=self.timeout) as response:
                result = json.load(response)
        except (HTTPError, URLError, TimeoutError, OSError, ValueError) as exc:
            raise LLMProviderError("Ollama request failed; check service, model and timeout.") from exc
        if not isinstance(result, dict) or result.get("error"):
            raise LLMProviderError("Ollama returned an error response.")
        if result.get("done") is not True or result.get("done_reason") == "length":
            raise LLMProviderError("Ollama generation was incomplete or truncated.")
        if not isinstance(result.get("response"), str) or not result["response"].strip():
            raise LLMProviderError("Ollama returned no generated text.")
        return result

    def generate(self, prompt: str, system: str, schema: dict) -> str:
        if not prompt.strip():
            raise ValueError("A non-empty prompt is required.")
        return self._request({
            "model": self.model, "prompt": prompt, "system": system,
            "format": schema, "stream": False,
            "options": {"temperature": 0, "num_predict": self.num_predict},
        })["response"]

    def response(self, prompt: str) -> dict:
        """Legacy entry point: return the Ollama response mapping."""
        if not prompt.strip():
            raise ValueError("A non-empty prompt is required.")
        return self._request({"model": self.model, "prompt": prompt, "stream": False,
                              "options": {"num_predict": self.num_predict}})


class Ollama_Client(OllamaProvider):
    """Backward-compatible class name used by earlier notebooks."""
