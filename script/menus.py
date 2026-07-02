def main_menu():
    print("\n" + "=" * 55)
    print("                    HUERGO POKEMON")
    print("=" * 55)
    print()
    print(" 1. View Pokedex")
    print(" 2. View Main Team")
    print(" 3. View PC")
    print(" 4. View Medals")
    print(" 5. Capture new Pokemon")
    print(" 6. Sort PC")
    print(" 7. Search Pokemon in Team")
    print(" 8. Send Pokemon to Pokemon Center")
    print(" 9. Transfer Pokemon to Professor Oak")
    print("10. Undo last transfer")
    print("11. Challenge Gym Leader")
    print("12. Manage Team")
    print("13. Exit system")
    print("=" * 55)

    try:
        option = int(input("Select an option: "))
        return option
    except:
        return"Invalid option"

def pokedex_select():
    pokedex_title()
    print("Select One of the following options: ")
    print("1. View full Pokedex")
    print("2. Search a Pokemon by his ID")
    print("3. Exit")
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"
    
def pokedex_title():
    print("==========================")
    print("         POKEDEX")
    print("==========================")
    print()


def enter_to_continue():
    input("Press enter to continue ")

def sorting_PC_title():
    print("==========================")
    print("     PC ORGANIZATION")
    print("==========================")
    print()

def main_team_title():
    print("=" * 45)
    print(" " * 16 + "MAIN TEAM")
    print("=" * 45)
    print()

def sorting_PC_menu():
    sorting_PC_title()
    print("How would you like to sort your PC?")
    print("1. Alphabetically")
    print("2. By Type")
    print("3. By CP")
    print("4. Exit")
    print()
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"
    
def catching_menu():
    print("==========================")
    print("      WILD POKEMON!")
    print("==========================")
    print()

def PC_title():
    print("==========================")
    print("        POKEMON PC")
    print("==========================")
    print()

def badges_menu():
    print("==========================")
    print("         BADGES")
    print("==========================")
    print()
    print("1. View Earned Badges")
    print("2. View All Badges")
    print()
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"
    
def earned_badges_title():
    print("==========================")
    print("      EARNED BADGES")
    print("==========================")
    print()

def all_badges_title():
    print("==========================")
    print("      ALL BADGES")
    print("==========================")
    print()
    print("Available Gym Badges:")
    print() 

def find_pokemon_title():
    print("==========================")
    print("     FIND A POKEMON")
    print("==========================")
    print()

def find_pokemon_menu():
    find_pokemon_title()
    print("Search for a Pokemon in your team.")
    print()
    try:
        pokemon_name = (input("Enter the Pokemon's name: ")).lower()
        return pokemon_name
    except:
        return "Invalid option"
    
def found_pokemon_menu(pokemon):
    print("==========================")
    print("    POKEMON FOUND")
    print("==========================")
    print()
    print(f"{pokemon.name} is in your team!")
    print(f"ID: {pokemon.id}")
    print(f"Type: {pokemon.type}")
    print(f"CP: {pokemon.CP}")
    print()
    enter_to_continue()

def not_found_menu(input):
    print("==========================")
    print("   POKEMON NOT FOUND")
    print("==========================")
    print()
    print(f"{input} is not in your team.")
    print()
    enter_to_continue()

def pokemon_center_title():
    print("=" * 45)
    print(" " * 13 + "POKEMON CENTER")
    print("=" * 45)

def pokemon_center_menu():
    pokemon_center_title()
    print()
    print("1. Heal Team")
    print("2. Exit")
    print()
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"
    
def professor_oak_transfer_title():
    print("=" * 45)
    print("        TRANSFER TO PROFESSOR OAK")
    print("=" * 45)

def professor_oak_transfer_menu():
    professor_oak_transfer_title()
    print()
    print("1. Transfer a Pokemon from your Team")
    print("2. Transfer a Pokemon from your PC")
    print("3. Undo Last Transfer")
    print("4. Exit")
    print()
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"

def gym_challenge_title():
    print("=" * 55)
    print("                    GYM CHALLENGE")
    print("=" * 55)
    print()

def gym_challenge_menu():
    gym_challenge_title()
    badges = [
    "Boulder Badge",
    "Cascade Badge",
    "Thunder Badge",
    "Rainbow Badge",
    "Soul Badge",
    "Marsh Badge",
    "Volcano Badge",
    "Earth Badge"
]
    print("Choose a Gym Leader:")
    print()
    print("1. Pewter Gym     - Brock      (Boulder Badge)")
    print("2. Cerulean Gym   - Misty      (Cascade Badge)")
    print("3. Vermilion Gym  - Lt. Surge  (Thunder Badge)")
    print("4. Celadon Gym    - Erika      (Rainbow Badge)")
    print("5. Fuchsia Gym    - Koga       (Soul Badge)")
    print("6. Saffron Gym    - Sabrina    (Marsh Badge)")
    print("7. Cinnabar Gym   - Blaine     (Volcano Badge)")
    print("8. Viridian Gym   - Giovanni   (Earth Badge)")
    print("9. Exit")
    print("=" * 55)

    try:
        option = int(input("Select a Gym: "))
        if 1 <= option <= 8:
            return badges[option - 1]
        elif option == 9:
            return None
        else:
            return "Invalid option"
    except:
        return "Invalid option"
    
def badge_earned_menu(badge):
    print("=" * 45)
    print(" " * 14 + "VICTORY!")
    print("=" * 45)
    print()
    print("Congratulations!")
    print(f"You defeated the Gym Leader!")
    print(f"You earned the {badge}!")
    print()


def badge_already_owned_menu(badge):
    print("=" * 45)
    print(" " * 10 + "BADGE ALREADY OWNED")
    print("=" * 45)
    print()
    print(f"You defeated the Gym Leader again!")
    print(f"You already have the {badge}.")
    print("No new badge was awarded.")
    print()


def badge_not_earned_menu():
    print("=" * 45)
    print(" " * 16 + "DEFEAT")
    print("=" * 45)
    print()
    print("You lost the Gym Battle.")
    print("Better luck next time!")
    print("No badge was earned.")
    print()

def wild_pokemon_title():
    print("=" * 45)
    print(" " * 13 + "WILD POKEMON")
    print("=" * 45)
    print()

def pokemon_caught_title():
    print("=" * 45)
    print(" " * 15 + "POKEMON CAUGHT")
    print("=" * 45)
    print()

def pokemon_escaped_title():
    print("=" * 45)
    print(" " * 15 + "POKEMON ESCAPED")
    print("=" * 45)
    print()

def manage_team_title():
    print("=" * 45)
    print(" " * 14 + "MANAGE TEAM")
    print("=" * 45)
    print()

def manage_team_menu():
    manage_team_title()
    print("What would you like to do?")
    print("1. View Team")
    print("2. Move a Pokemon to PC")
    print("3. Bring a Pokemon from PC")
    print("4. Swap two Pokemon positions")
    print("5. Exit")
    print()
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"