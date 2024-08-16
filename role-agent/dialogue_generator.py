from model_interaction import model_interaction

class DialogueGenerator:
    def __init__(self, character1, character2):
        self.characters = [character1, character2]
        self.messages = []
        self.current_character = 0

    def generate_dialogue(self, user_input, num_turns=1):
        dialogue = []
        for _ in range(num_turns):
            for i in range(2):
                character = self.characters[self.current_character]
                messages = [
                    {"role": "system", "content": character['prompt']},
                    *self.messages,
                    {"role": "user", "content": user_input if i == 0 else dialogue[-1]['content']}
                ]
                response = model_interaction.generate_response(messages)
                if response:
                    dialogue_entry = {
                        "speaker": character['Name'],
                        "content": response
                    }
                    dialogue.append(dialogue_entry)
                    self.messages.append({"role": "assistant", "content": response})
                else:
                    dialogue_entry = {
                        "speaker": character['Name'],
                        "content": "[No response generated]"
                    }
                    dialogue.append(dialogue_entry)
                self.current_character = (self.current_character + 1) % 2
        return dialogue

    def reset_conversation(self):
        self.messages = []
        self.current_character = 0