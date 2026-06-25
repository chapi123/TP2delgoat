def main_menu():
    print("\n" + "=" * 55)
    print("                    HUERGO POKEMON")
    print("=" * 55)
    print(" 1. View Pokédex")
    print(" 2. View Main Team")
    print(" 3. View PC")
    print(" 4. Capture new Pokémon")
    print(" 5. Sort PC")
    print(" 6. Search Pokémon in Team")
    print(" 7. Send Pokémon to Pokémon Center")
    print(" 8. Transfer Pokémon to Professor Oak")
    print(" 9. Undo last transfer")
    print("10. Challenge Gym Leader")
    print("11. Exit system")
    print("=" * 55)

    try:
        option = int(input("Select an option: "))
        return option
    except:
        return"Invalid option"

def pokedex_select():
    print("Select One of the following options: ")
    print("1. View full Pokedex")
    print("2. Search a Pokemon by his ID")
    print("3. Exit")
    try:
        option = int(input("Select an option: "))
        return option
    except:
        return "Invalid option"

def enter_to_continue():
    input("Press enter to continue ")