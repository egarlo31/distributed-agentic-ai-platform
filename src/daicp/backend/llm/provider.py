"""Runtime-independent interface for structured local model generation."""
from abc import ABC, abstractmethod


class LLMProviderError(RuntimeError):
    """The inference service failed or returned an invalid transport response."""


class LLMProvider(ABC):
    """Providers return JSON text; RCA owns semantic output validation."""

    @abstractmethod
    def generate(self, prompt: str, system: str, schema: dict) -> str:
        """Generate one complete JSON object constrained by the supplied schema."""
