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

def standardize_keys(character_dict):
    key_mapping = {
        'name': 'Name',
        'age': 'Age',
        'occupation': 'Occupation',
        'personality_traits': 'Personality_traits',
        'background': 'Background',
        'goals_and_motivations': 'Goals_and_motivations',
        'speaking_style': 'Speaking_style'
    }
    return {key_mapping.get(k, k): v for k, v in character_dict.items()}

def generate_character(text, language="en"):
    if language == "en":
        prompt = f"""
Based on the following text, create a detailed character profile in English. Include:
1. Name
2. Age
3. Occupation
4. Personality traits
5. Background
6. Goals and motivations
7. Speaking style

Text:
{text}

Please format the response ONLY as a Python dictionary named 'character_profile', without any additional text or code blocks. Use English keys for the dictionary.
"""
    elif language == "zh":
        prompt = f"""
根据以下文本，用中文创建一个详细的角色简介。包括：
1. Name (姓名)
2. Age (年龄)
3. Occupation (职业)
4. Personality_traits (性格特征)
5. Background (背景)
6. Goals_and_motivations (目标和动机)
7. Speaking_style (说话风格)

文本：
{text}

请将响应仅格式化为名为'character_profile'的Python字典，不要包含任何其他文本或代码块。请使用英文作为字典的键名。
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
                character_dict = standardize_keys(character_dict)
                if language == "en":
                    character_dict['prompt'] = f"""You are {character_dict['Name']}, {character_dict['Age']}-year-old {character_dict['Occupation']}. 
Your personality traits are: {', '.join(character_dict['Personality_traits'])}. 
Your background is: {character_dict['Background']}. 
Your goals and motivations are: {', '.join(character_dict['Goals_and_motivations'])}. 
Your speaking style is: {character_dict['Speaking_style']}.
Respond to messages in character, based on this profile. Do not refer to yourself in the third person or mention that you are role-playing. Speak directly as the character would."""
                elif language == "zh":
                    character_dict['prompt'] = f"""你是{character_dict['Name']}，{character_dict['Age']}岁的{character_dict['Occupation']}。
你的性格特征是：{', '.join(character_dict['Personality_traits'])}。
你的背景是：{character_dict['Background']}。
你的目标和动机是：{', '.join(character_dict['Goals_and_motivations'])}。
你的说话风格是：{character_dict['Speaking_style']}。
基于这个角色设定回应消息。不要以第三人称提及自己，也不要提到你在角色扮演。直接以角色的方式说话。"""
                return character_dict
    
    print("Failed to generate or parse the character profile.")
    return None