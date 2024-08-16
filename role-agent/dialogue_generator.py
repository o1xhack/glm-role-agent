from model_interaction import model_interaction

class DialogueGenerator:
    def __init__(self, character1, character2, language="en"):
        self.characters = [character1, character2]
        self.messages = []
        self.current_character = 0
        self.language = language

    def generate_dialogue(self, user_input, num_turns=1):
        dialogue = []
        topic = user_input  # 记录话题
        for _ in range(num_turns):
            for i in range(2):
                character = self.characters[self.current_character]
                messages = [
                    {"role": "system", "content": character['prompt']},
                    *self.messages,
                    {"role": "user", "content": user_input if i == 0 else dialogue[-1]['content']}
                ]
                if self.language == "zh":
                    messages.append({"role": "system", "content": "请用中文回答。"})
                response = model_interaction.generate_response(messages)
                if response:
                    response = self.clean_response(response)
                    dialogue_entry = {
                        "speaker": character['Name'],
                        "content": response
                    }
                    dialogue.append(dialogue_entry)
                    self.messages.append({"role": "assistant", "content": response})
                else:
                    dialogue_entry = {
                        "speaker": character['Name'],
                        "content": "[No response generated]" if self.language == "en" else "[未生成回复]"
                    }
                    dialogue.append(dialogue_entry)
                self.current_character = (self.current_character + 1) % 2
        return topic, dialogue  # 返回话题和对话

    def clean_response(self, response):
        lines = response.split('\n')
        cleaned_lines = [line for line in lines if not line.startswith(("作为", "As a", "Joe Biden:", "Donald Trump:"))]
        return '\n'.join(cleaned_lines).strip()

    def reset_conversation(self):
        self.messages = []
        self.current_character = 0