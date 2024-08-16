from model_interaction import model_interaction

class DialogueGenerator:
    def __init__(self, character1, character2, language="en"):
        self.characters = [character1, character2]
        self.messages = []
        self.current_character = 0
        self.language = language

    def generate_single_response(self, user_input):
        character = self.characters[self.current_character]
        context = "\n".join([msg["content"] for msg in self.messages[-3:]])
        if self.language == "zh":
            prompt = f"根据最近的对话内容：\n{context}\n\n当前话题：{user_input}\n\n使用中文，请以角色的方式自然地回应这个话题："
        else:
            prompt = f"Based on the recent conversation:\n{context}\n\nCurrent topic: {user_input}\n\nUse English, Respond naturally to this topic as your character:"

        messages = [
            {"role": "system", "content": character['prompt']},
            {"role": "user", "content": prompt}
        ]
        
        response = model_interaction.generate_response(messages, temperature=0.9)
        
        if response:
            response = self.clean_response(response)
            dialogue_entry = {
                "speaker": character['Name'],
                "content": response
            }
            self.messages.append({"role": "assistant", "content": response})
        else:
            dialogue_entry = {
                "speaker": character['Name'],
                "content": "[No response generated]" if self.language == "en" else "[未生成回复]"
            }
        self.current_character = (self.current_character + 1) % 2
        return dialogue_entry

    def clean_response(self, response):
        lines = response.split('\n')
        cleaned_lines = [line for line in lines if not line.startswith(("作为", "As a", "Joe Biden:", "Donald Trump:"))]
        return '\n'.join(cleaned_lines).strip()

    def reset_conversation(self):
        self.messages = []
        self.current_character = 0