import json
from datetime import datetime

def save_dialogue(characters, dialogue, filename=None):
    if filename is None:
        filename = f"dialogue_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    data = {
        "characters": characters,
        "dialogue": dialogue
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return filename

def format_dialogue(dialogue):
    formatted_dialogue = []
    for entry in dialogue:
        formatted_entry = f"{entry['speaker']}:\n{entry['content']}\n"
        formatted_dialogue.append(formatted_entry)
    return "\n".join(formatted_dialogue)