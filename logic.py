import storage
import script.pokemons
import script.menus as menus
import team
import os, random, time, sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def view_pokedex(pokedex):
    clear()
    option1 = menus.pokedex_select()
    clear()
    if option1 == 1:
        menus.pokedex_title()
        for pokemon in pokedex.values():
            print(
                "ID:", pokemon.id,
                "Name:", pokemon.name,
                "Type:", pokemon.type,
                "CP:", pokemon.CP
            )
        print("")
        menus.enter_to_continue()
    elif option1 == 2:
        clear()
        menus.pokedex_title()
        selected = int(input('Insert a Pokemon ID: '))
        pokemon = pokedex.search_pokemon_by_id(selected)
        if pokemon:
            print(
                "ID:", pokemon.id,
                "Name:", pokemon.name,
                "Type:", pokemon.type,
                "CP:", pokemon.CP,
            )
            menus.enter_to_continue()
        else:
            print("Pokemon for ID",selected,"was not found")
            menus.enter_to_continue()
    elif option1 == 3:
        pass
    else: 
        print("Invalid option")
        menus.enter_to_continue()

def view_main_team(team_l, pokedex):
    clear()
    menus.main_team_title()
    team.show_team(team_l)
    print()
    menus.enter_to_continue()

def view_PC(PC):
    clear()
    menus.PC_title()
    if PC.count_nodes() != 0:
       PC.print_PC_values()  
    else:
        print("Your PC is Empty")
    print()
    menus.enter_to_continue()

def view_medals(obtained_medals, all_medals):
    clear()
    while True:
        option1 = menus.badges_menu()
        if option1 == 1:
            clear()
            menus.earned_badges_title()
            counter = 1
            for i in obtained_medals.values():
                print(f"{counter}. {i}")
                counter += 1
            print(f"Progress:{counter-1}/8")
            print("")
            menus.enter_to_continue()
            break
        elif option1 == 2:
            clear()
            menus.all_badges_title()
            all_medals.print_set()
            print("")
            menus.enter_to_continue()
            break
        else:
            print("Invalid option")
            menus.enter_to_continue()

def capture_new_pokemon(pokedex, PC, team_l):
    clear()
    selected = script.pokemons.select_random_pokemon(pokedex)
    menus.wild_pokemon_title()
    print(f"A wild {selected.name} has appeared!")
    print(f"ID: {selected.id}, Type: {selected.type}, CP: {selected.CP}")

    while True:
        option1 = input(f"Would you like to catch {selected.name}? (Y/N): ").lower()

        if option1 == "y":
            success = random.randint(0, 1)

            if success == 1:
                clear()
                menus.pokemon_caught_title()
                print(f"Gotcha! {selected.name} was caught!")
                print("Where would you like to store this Pokemon?")
                print("1. Main Team")
                print("2. PC Storage")
                while True:
                    try:
                        option2 = int(input("Select an option: "))

                        if option2 == 1:
                            clear()
                            menus.pokemon_caught_title()

                            result = team.add_pokemon_team(team_l, selected, PC)

                            if result == "added":
                                print(f"{selected.name} joined your party!")

                            elif result == "full":
                                print("Your Main Team is full")
                                print(f"{selected.name} was sent to the PC!")

                            break

                        elif option2 == 2:
                            clear()
                            menus.pokemon_caught_title()
                            print(f"{selected.name} was sent to the PC!")
                            storage.add_pokemon_PC(PC, selected)
                            break

                        else:
                            print("Invalid option.")

                    except ValueError:
                        print("Invalid option.")
                print()
                menus.enter_to_continue()

            else:
                clear()
                menus.pokemon_escaped_title()
                print(f"Oh no! {selected.name} escaped!")
                menus.enter_to_continue()
            break

        elif option1 == "n":
            break

        else:
            print("Invalid option. Please enter Y or N.")

def sort_PC(PC):
    clear()
    if PC.count_nodes() != 0:
        while True:
            option1 = menus.sorting_PC_menu()
            if option1 == 1:
                clear()
                menus.sorting_PC_title()
                PC.bubble_sort()
                print("PC has been sorted alphabetically")
                print()
                PC.print_PC_values()
                print()
                menus.enter_to_continue()
                break
            elif option1 == 2:
                clear()
                menus.sorting_PC_title()
                PC.insertion_sort()
                print("PC has been sorted by Type")
                print()
                PC.print_PC_values()
                print()
                menus.enter_to_continue()
                break
            elif option1 == 3:
                clear()
                menus.sorting_PC_title()
                PC.quick_sort_nodes()
                print("PC has been sorted by CP")
                print()
                PC.print_PC_values()
                print()
                menus.enter_to_continue()
                break
            elif option1 == 4:
                break
            else:
                print("Invalid option")
                menus.enter_to_continue()
    else:
        menus.sorting_PC_title()
        print("Your PC is Empty")
        menus.enter_to_continue()

def search_pokemon_in_team(team_l):
    clear()
    option1 = menus.find_pokemon_menu()
    found, index = team.search(team_l, option1)

    if found:
        clear()
        menus.found_pokemon_menu(index)
    else:
        clear()
        menus.not_found_menu(option1)

def send_pokemon_to_pokemon_center(team_l, center):
    if not team.is_empty(team_l):
        clear()
        while True:
            option1 = menus.pokemon_center_menu()
            if option1 == 1:
                clear()
                menus.pokemon_center_title()
                print("Healing your Pokemons...")
                for i in team_l:
                    center.enqueue(i)
                for i in center.values():
                    clear()
                    menus.pokemon_center_title()
                    healed = center.dequeue()
                    if healed is not None:
                        print(f"{healed.name} is being healed...")
                        time.sleep(1)
                        print()
                        print(f"{healed.name} was healed")
                        time.sleep(1)
                        
                clear()
                menus.pokemon_center_title()
                print()
                print("Your Pokemons have been Healed!")
                print()
                menus.enter_to_continue()
                break
            elif option1 == 2:
                break
            else: 
                print("Invalid option")
                menus.enter_to_continue()
    else:
        clear()
        menus.pokemon_center_title()
        print("Your team is empty")
        print()
        menus.enter_to_continue()

def transfer_pokemon_to_professor_oak(team_l, PC, professor_stack):
    clear()

    while True:
        option1 = menus.professor_oak_transfer_menu()

        if option1 == 1:
            clear()

            if team.is_empty(team_l):
                menus.professor_oak_transfer_title()
                print("Your Team is empty")
                print()
                menus.enter_to_continue()
                continue

            while True:
                try:
                    clear()
                    menus.professor_oak_transfer_title()
                    team.show_team(team_l)
                    print()
                    option2 = int(input("Select a Pokemon's ID: "))
                    break
                except:
                    print("Invalid option")
                    print()
                    menus.enter_to_continue()

            found = False

            for i in team_l:
                if i is not None and i.id == option2:
                    found = True

                    if professor_stack.push(i):
                        clear()
                        menus.professor_oak_transfer_title()
                        print("Transfering to professor Oak...")
                        time.sleep(2)

                        clear()
                        menus.professor_oak_transfer_title()
                        print(f"{i.name} was transfered to professor Oak")

                        option3 = input("Cancel Transfer? (Y/N): ")

                        if option3.lower() == "y":
                            professor_stack.pop()
                            print(f"{i.name} was transfered back to your Team")
                            menus.enter_to_continue()
                            return

                        elif option3.lower() == "n":
                            index = team_l.index(i)
                            team_l[index] = None
                            menus.enter_to_continue()
                            return

                        else:
                            print("Invalid Option")
                            print()
                            menus.enter_to_continue()
                            break

                    else:
                        print("Professor Oak has 5 Pokemons already")
                        print()
                        menus.enter_to_continue()
                        return

            if not found:
                print(f"Pokemon with {option2} ID was not found")
                print()
                menus.enter_to_continue()

        elif option1 == 2:

            if PC.count_nodes() == 0:
                print("Your PC is empty")
                print()
                menus.enter_to_continue()
                continue

            while True:
                try:
                    clear()
                    menus.professor_oak_transfer_title()
                    PC.print_PC_values()
                    print()
                    option2 = int(input("Select a Pokemon's ID: "))
                    break
                except:
                    print("Invalid option")
                    print()
                    menus.enter_to_continue()

            found = False

            for i in PC.values():
                if i.id == option2:
                    found = True

                    if professor_stack.push(i):
                        clear()
                        menus.professor_oak_transfer_title()
                        print("Transfering to professor Oak...")
                        time.sleep(2)

                        clear()
                        menus.professor_oak_transfer_title()
                        print(f"{i.name} was transfered to professor Oak")

                        option3 = input("Cancel Transfer? (Y/N): ")

                        if option3.lower() == "y":
                            professor_stack.pop()
                            print(f"{i.name} was transfered back to your PC")
                            menus.enter_to_continue()
                            return

                        elif option3.lower() == "n":
                            PC.delete(i)
                            menus.enter_to_continue()
                            return

                        else:
                            print("Invalid Option")
                            print()
                            menus.enter_to_continue()
                            break

                    else:
                        print("Professor Oak has 5 Pokemons already")
                        print()
                        menus.enter_to_continue()
                        return

            if not found:
                print(f"Pokemon with {option2} ID was not found")
                print()
                menus.enter_to_continue()

def undo_last_transfer(professor_stack, PC):
    clear()
    menus.professor_oak_transfer_title()
    popped = professor_stack.pop()
    if popped is None:
        print()
        print("Professor Oak has no Pokemons")
        print()
        menus.enter_to_continue()
        return
    PC.add_node(popped)
    print(f"{popped.name} was tranfered back to your PC")
    print()
    menus.enter_to_continue()
    return

def challenge_gym_leader(obtained_medals, team_l):
    if team.is_empty(team_l):
        clear()
        menus.gym_challenge_title()
        print("You cannot fight, your Team is Empty")
        print()
        menus.enter_to_continue()
        return

    while True:
        clear()
        option1 = menus.gym_challenge_menu()

        if option1 is None:
            return

        if option1 == "Invalid option":
            clear()
            menus.gym_challenge_title()
            print("Invalid option")
            print()
            menus.enter_to_continue()
            continue

        success = random.randint(0, 1)

        if success == 1:
            if obtained_medals.put(option1):
                clear()
                menus.badge_earned_menu(option1)
            else:
                clear()
                menus.badge_already_owned_menu(option1)
        else:
            clear()
            menus.badge_not_earned_menu()

        menus.enter_to_continue()
        return

def manage_team(team_l, PC):
    clear()
    while True:
        option1 = menus.manage_team_menu()

        if option1 == 1:
            clear()
            menus.manage_team_title()
            team.show_team(team_l)
            print()
            menus.enter_to_continue()
            clear()

        elif option1 == 2:
            clear()
            menus.manage_team_title()
            if team.is_empty(team_l):
                print("Your Team is empty")
                menus.enter_to_continue()
                continue
            clear()

            team.show_team(team_l)
            print()
            try:
                index = int(input("Select a slot number to move to PC (1-6): ")) - 1
                if index < 0 or index >= len(team_l) or team_l[index] is None:
                    print("Invalid slot")
                    menus.enter_to_continue()
                    continue
            except ValueError:
                print("Invalid option")
                menus.enter_to_continue()
                continue

            pokemon = team_l[index]
            team.move_to_PC(team_l, index, PC)
            print(f"{pokemon.name} was moved to the PC")
            menus.enter_to_continue()
            clear()

        elif option1 == 3:
            clear()
            menus.manage_team_title()
            if PC.count_nodes() == 0:
                print("Your PC is empty")
                menus.enter_to_continue()
                continue
            clear()
            PC.print_PC_values()
            print()
            try:
                selected_id = int(input("Select a Pokemon's ID: "))
            except ValueError:
                print("Invalid option")
                menus.enter_to_continue()
                continue

            success, result = team.bring_from_PC(team_l, PC, selected_id)
            if success:
                print(f"{result.name} joined your Team!")
            elif result == "full":
                print("Your Team is full")
            else:
                print("Pokemon not found in PC")
            menus.enter_to_continue()
            clear()

        elif option1 == 4:
            clear()
            menus.manage_team_title()
            if team.is_empty(team_l):
                print("Your Team is empty")
                menus.enter_to_continue()
                continue
            clear()

            team.show_team(team_l)
            print()
            try:
                i = int(input("Select first slot: ")) - 1
                j = int(input("Select second slot: ")) - 1
                if not (0 <= i < len(team_l)) or not (0 <= j < len(team_l)):
                    raise ValueError
            except ValueError:
                print("Invalid option")
                menus.enter_to_continue()
                continue

            team.swap_positions(team_l, i, j)
            print("Positions swapped")
            menus.enter_to_continue()
            clear()

        elif option1 == 5:
            break

        else:
            print("Invalid option")
            menus.enter_to_continue()
            clear()

def exit():
    clear()
    print("Thanks for playing")
    sys.exit()

def else_():
    print("Invalid option")
    menus.enter_to_continue()

