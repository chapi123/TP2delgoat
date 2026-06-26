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
    print("12. Exit system")
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

def sorting_PC_menu():
    sorting_PC_title()
    print("How would you like to sort your PC?")
    print("1. Alphabetically")
    print("2. By CP")
    print("3. By Type")
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