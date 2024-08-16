import os
from zhipuai import ZhipuAI

class ModelInteraction:
    def __init__(self):
        api_key = os.getenv("ZHIPUAI_API_KEY")
        if not api_key:
            raise ValueError("ZHIPUAI_API_KEY environment variable is not set")
        self.client = ZhipuAI(api_key=api_key)

    def generate_response(self, messages, model="glm-4", max_tokens=2000, temperature=0.7):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                stream=False,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in API call: {e}")
            return None

model_interaction = ModelInteraction()