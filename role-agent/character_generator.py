import re
import ast
from model_interaction import model_interaction

def clean_and_parse_dict(dict_str):
    dict_str = re.sub(r'""".*?"""', '""', dict_str, flags=re.DOTALL)
    dict_str = re.sub(r'(\w+):', r'"\1":', dict_str)
    dict_str = re.sub(r',\s*}', '}', dict_str)
    try:
        return ast.literal_eval(dict_str)
    except:
        return None

def generate_character(text):
    prompt = f"""
Based on the following text, create a detailed character profile. Include:
1. Name
2. Age
3. Occupation
4. Personality traits
5. Background
6. Goals and motivations
7. Speaking style

Text:
{text}

Please format the response ONLY as a Python dictionary named 'character_profile', without any additional text or code blocks.
"""
    messages = [{"role": "user", "content": prompt}]
    response = model_interaction.generate_response(messages)
    if response:
        print("Raw response from model:")
        print(response)
        
        dict_match = re.search(r'character_profile\s*=\s*({.*})', response, re.DOTALL)
        if dict_match:
            dict_str = dict_match.group(1)
            character_dict = clean_and_parse_dict(dict_str)
            if character_dict:
                character_dict['prompt'] = f"""You are {character_dict['Name']}, a {character_dict['Age']}-year-old {character_dict['Occupation']}. 
Your personality traits include {', '.join(character_dict['Personality traits'])}. 
Your background is: {character_dict['Background']}. 
Your goals and motivations are: {character_dict['Goals and motivations']}. 
Your speaking style is {character_dict['Speaking style']}.
Respond to messages in character, based on this profile."""
                return character_dict
    
    print("Failed to generate or parse the character profile.")
    return None