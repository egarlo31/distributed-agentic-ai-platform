# LLM Provider

`LLMProvider` defines `generate(prompt, system, schema) -> str`. `OllamaProvider`
implements it through `POST /api/generate` with a non-streaming response, JSON schema,
zero temperature, a timeout, and a generation limit. Importing or constructing the
adapter does not download models or start services.

```python
from daicp.backend.llm import OllamaProvider
provider = OllamaProvider(model="qwen3:8b", host="http://localhost:11434", timeout=120)
```

Ollama must be running and the model installed before incident analysis. Transport
or server errors, missing generated text, and truncated generations raise
`LLMProviderError`. Failed generations are not retried automatically. RCA validates
the generated structure and citation IDs; this does not establish factual correctness.

`Ollama_Client(model).response(prompt)` retains the previous class name and entry
point. It now returns the Ollama HTTP response as a dictionary, with generated text
in `response`. New consumers should use `LLMProvider.generate`.

HTTP contract reference: [Ollama Generate](https://docs.ollama.com/api/generate).
