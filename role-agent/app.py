from flask import Flask, jsonify, request
from flask_cors import CORS
from character_generator import generate_character
from dialogue_generator import DialogueGenerator
from data_saver import save_dialogue
from model_interaction import model_interaction
from main import text1, text2  # 从 main.py 导入 text1 和 text2

app = Flask(__name__)
CORS(app)

# 新增API，返回默认文本
@app.route('/api/get_default_texts', methods=['GET'])
def get_default_texts():
    return jsonify({"text1": text1, "text2": text2})

# 生成角色的 API
@app.route('/api/generate_character', methods=['POST'])
def generate_character_api():
    data = request.json
    
    # 如果前端没有提供文本，强制使用 main.py 中的默认文本
    if not data.get('text'):
        text = text1 if 'character1' in data else text2
    else:
        text = data['text']
    
    language = data.get('language', 'en')
    
    print(f"Using text for character generation: {text}")  # 调试日志
    
    # 调用 generate_character 函数生成角色
    character_profile = generate_character(text, language)
    if character_profile:
        return jsonify(character_profile)
    else:
        return jsonify({"error": "Character generation failed"}), 500


# 生成对话的 API
@app.route('/api/generate_dialogue', methods=['POST'])
def generate_dialogue_api():
    data = request.json
    character1 = data.get('character1')
    character2 = data.get('character2')
    topic = data.get('topic', '')
    language = data.get('language', 'en')
    
    # 创建 DialogueGenerator 对象并生成对话
    dialogue_gen = DialogueGenerator(character1, character2, language)
    dialogue = []

    for _ in range(6):  # 每个角色各有3次对话轮数
        response = dialogue_gen.generate_single_response(topic if len(dialogue) == 0 else dialogue[-1]['content'])
        dialogue.append(response)
    
    return jsonify(dialogue)

# 保存对话的 API
@app.route('/api/save_dialogue', methods=['POST'])
def save_dialogue_api():
    data = request.json
    characters = data.get('characters')
    dialogues = data.get('dialogues')

    # 调用 save_dialogue 函数保存对话
    filename = save_dialogue(characters, dialogues)
    return jsonify({"message": "Dialogues saved", "filename": filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)