class ContentEngine:
    def __init__(self, client):
        self.client = client

    def generate_caption(self, product: str, objective: str):
        prompt = f"""
        Create an Instagram marketing caption.
        Product: {product}
        Objective: {objective}
        Return caption, hashtags and call to action.
        """
        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )
        return response.output_text

    def analyze_content(self, content: str):
        return {
            "content": content,
            "analysis": "AI analysis pending"
        }
