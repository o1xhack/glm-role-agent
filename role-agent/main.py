import argparse
from character_generator import generate_character
from dialogue_generator import DialogueGenerator
from data_saver import save_dialogue, format_dialogue

def main():
    parser = argparse.ArgumentParser(description="Generate character dialogues")
    parser.add_argument("--lan", choices=["en", "zh"], default="en", help="Language for generation (en: English, zh: Chinese)")
    args = parser.parse_args()

    language = args.lan

    print("Generating characters...")
    
    text1 = """
    Donald Trump, the 45th President of the United States. Known for his background in real estate and reality TV, 
    he entered politics and won the 2016 presidential election. His presidency was marked by controversial policies, 
    active use of social media, and a distinctive communication style. He's known for his "America First" agenda, 
    strong stance on immigration, and unconventional approach to international relations.
    """
    
    text2 = """
    Joe Biden, the 46th and current President of the United States. With a long career in politics, including serving 
    as a Senator and as Vice President under Barack Obama, he won the 2020 presidential election. Known for his 
    experience in foreign policy, emphasis on unity and bipartisanship, and more traditional political approach. 
    He's focused on issues like climate change, healthcare reform, and rebuilding international alliances.
    """

    character1 = generate_character(text1, language)
    character2 = generate_character(text2, language)

    if character1 is None or character2 is None:
        print("Failed to generate one or both characters. Exiting.")
        return

    print(f"Character 1: {character1['Name']}")
    print(f"Character 2: {character2['Name']}")

    dialogue_gen = DialogueGenerator(character1, character2, language)

    all_dialogues = []
    while True:
        user_input = input("\nEnter a topic or scenario (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break

        print("\nGenerating dialogue...")
        topic = user_input
        dialogue = []
        
        for _ in range(6):  # 3 turns for each character
            response = dialogue_gen.generate_single_response(user_input if len(dialogue) == 0 else dialogue[-1]['content'])
            dialogue.append(response)
            print(f"\n{response['speaker']}:\n{response['content']}")
            
        all_dialogues.append({"topic": topic, "dialogue": dialogue})

        print("\nFull Generated Dialogue:")
        print(f"Topic: {topic}")
        print(format_dialogue(dialogue))

    if all_dialogues:
        print("\nSaving dialogues...")
        filename = save_dialogue([character1, character2], all_dialogues)
        print(f"Dialogues saved to {filename}")

if __name__ == "__main__":
    main()