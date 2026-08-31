from openai import OpenAI

class CaptionGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(self, product: str, goal: str):
        prompt = f"Create Instagram caption for {product}. Goal: {goal}"
        return prompt
