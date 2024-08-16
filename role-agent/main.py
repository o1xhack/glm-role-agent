from character_generator import generate_character
from dialogue_generator import DialogueGenerator
from data_saver import save_dialogue, format_dialogue

def main():
    print("Generating characters...")
    
    text1 = """
    A brilliant but eccentric scientist who spends most of her time in the lab. 
    She's known for her groundbreaking research in quantum physics and her peculiar habit of talking to her plants.
    Despite her intellectual prowess, she struggles with social interactions and often finds solace in her work.
    """
    
    text2 = """
    A charismatic and ambitious politician with a secret passion for abstract art. 
    He's climbing the ranks in the local government, known for his persuasive speeches and ability to connect with people.
    However, he harbors doubts about the impact of his work and often contemplates leaving politics to pursue his artistic dreams.
    """

    character1 = generate_character(text1)
    character2 = generate_character(text2)

    if character1 is None or character2 is None:
        print("Failed to generate one or both characters. Exiting.")
        return

    print(f"Character 1: {character1['Name']}")
    print(f"Character 2: {character2['Name']}")

    dialogue_gen = DialogueGenerator(character1, character2)

    all_dialogue = []
    while True:
        user_input = input("\nEnter a topic or scenario (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break

        print("\nGenerating dialogue...")
        dialogue = dialogue_gen.generate_dialogue(user_input, num_turns=3)
        all_dialogue.extend(dialogue)

        print("\nGenerated Dialogue:")
        print(format_dialogue(dialogue))

    if all_dialogue:
        print("\nSaving dialogue...")
        filename = save_dialogue([character1, character2], all_dialogue)
        print(f"Dialogue saved to {filename}")

if __name__ == "__main__":
    main()