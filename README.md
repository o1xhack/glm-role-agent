# Role-Playing Dialogue Generator

English | [简体中文](README-CN.md) | [繁體中文](README-ZH-HANT.md) | [日本語](README-JA.md) | 

This project is a Python-based tool that generates role-playing dialogues between two characters. While it's initially set up to simulate conversations between Donald Trump and Joe Biden, it can be easily modified to use any two characters of your choice.

## Features

- **Customizable Characters**: Although initially set up for Trump and Biden, you can easily modify the character descriptions to create dialogues between any two characters.
- **Character Generation**: Creates detailed character profiles based on provided descriptions, including personality traits, background, goals, and speaking style.
- **Dynamic Dialogue Generation**: Generates realistic, context-aware conversations between the characters.
- **Bilingual Support**: Supports both English and Chinese languages for character generation and dialogues.
- **Customizable Topics**: Allows users to input custom topics or scenarios for the characters to discuss.
- **Context Awareness**: Maintains conversation context, allowing for coherent multi-turn dialogues.
- **JSON Output**: Saves generated dialogues and character profiles in JSON format for easy parsing and analysis.
- **Interactive Mode**: Provides an interactive command-line interface for users to guide the conversation.
- **Flexible Character Switching**: Alternates between characters automatically during the dialogue generation.
- **Configurable Parameters**: Allows adjustment of model parameters like temperature for varied dialogue generation.

## Requirements

- Python 3.7+
- `zhipuai` library
- GLM-4 API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/o1xhack/glm-role-agent
   cd glm-role-agent
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your GLM-4 API key:
   
   It's recommended to set your API key in your local environment variables. You can do this by adding the following line to your `~/.bashrc`, `~/.zshrc`, or equivalent shell configuration file:

   ```
   export ZHIPUAI_API_KEY='your-api-key-here'
   ```

   After adding this line, remember to reload your shell configuration or restart your terminal.

   Alternatively, if you haven't set up the environment variable, you can export it temporarily before running the script:

   ```
   export ZHIPUAI_API_KEY='your-api-key-here'
   python main.py --lan=en
   ```

   Note: Replace 'your-api-key-here' with your actual GLM-4 API key.


## Usage

Run the main script with the desired language option:

```
python main.py --lan=en  # For English
python main.py --lan=zh  # For Chinese
```

Follow the prompts to enter conversation topics. Type 'quit' to end the dialogue generation.

## Customizing Characters

To change the characters used in the dialogue:

1. Open the `main.py` file.
2. Locate the `text1` and `text2` variables (around line 20).
3. Replace the content of these variables with descriptions of your desired characters.
4. Save the file and run the script as usual.

For example, to create a dialogue between Einstein and Newton, you might change the descriptions to:

```python
text1 = """
Albert Einstein, the renowned physicist known for his theory of relativity. 
He revolutionized our understanding of space, time, and gravity. 
Einstein was known for his thought experiments and his ability to explain 
complex ideas in simple terms.
"""

text2 = """
Sir Isaac Newton, the English physicist and mathematician who laid the 
foundations of classical mechanics. He discovered the laws of motion and 
universal gravitation, developed calculus, and made breakthroughs in optics. 
Newton was known for his methodical approach and his famous quote 
"If I have seen further it is by standing on the shoulders of Giants."
"""
```

## File Structure

- `main.py`: The main script to run the dialogue generator
- `character_generator.py`: Generates character profiles
- `dialogue_generator.py`: Handles the dialogue generation logic
- `model_interaction.py`: Manages interactions with the GLM-4 model
- `data_saver.py`: Handles saving and formatting of dialogues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.