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