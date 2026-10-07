import json
import os

# --- FILE READING FUNCTIONS ---

def display_text_file(filename):
    """Reads and prints the contents of a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"[Error: {filename} is missing!]")

# --- SAVE & LOAD FUNCTIONS ---

def save_game(player_name, game_state):
    """Saves the game state dictionary to a JSON text file."""
    filename = f"{player_name}_save.txt"
    with open(filename, 'w') as file:
        json.dump(game_state, file)
    print(f"\nGame saved successfully for {player_name}!")

def load_game(player_name):
    """Loads the game state from a JSON text file if it exists."""
    filename = f"{player_name}_save.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            game_state = json.load(file)
        print(f"\nWelcome back, {player_name}! Game loaded.")
        return game_state
    else:
        print(f"\nNo save file found for '{player_name}'.")
        return None

# --- MAIN MENU & GAME LOOP ---

def main():
    display_text_file("intro.txt")
    
    # Default game state for a new player
    game_state = {
        "level": 1,
        "health": 100,
        "inventory": []
    }
    
    print("\n1. New Game")
    print("2. Load Game")
    choice = input("> ")
    
    if choice == '1':
        player_name = input("Enter your name: ")
        display_text_file("instructions.txt")
        print("\nStarting a new adventure...")
        
    elif choice == '2':
        player_name = input("Enter your save name/code: ")
        loaded_state = load_game(player_name)
        if loaded_state:
            game_state = loaded_state
        else:
            print("Starting a new game instead...")
            display_text_file("instructions.txt")
            
    # Mock Game Loop
    while True:
        print(f"\n[Player: {player_name} | HP: {game_state['health']} | Level: {game_state['level']}]")
        action = input("What do you want to do? (type 'save' or 'quit'): ").lower()
        
        if action == 'save':
            save_game(player_name, game_state)
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            # Simulate playing the game
            print("You explore the area...")
            game_state["health"] -= 5
            game_state["level"] += 1

if __name__ == "__main__":
    main()