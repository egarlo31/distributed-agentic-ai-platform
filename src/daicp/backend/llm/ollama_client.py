import ollama


model = "qwen3:8b"
prompt = "que significa nada"

class Ollama_Client:
    """Client for local LLM inference through Ollama."""
    def __init__(self, model):
        self.model = model

    def response(self, prompt):
        """Generate and return a response for the given prompt."""
        response = ollama.generate(model=self.model, prompt=prompt)
        return response