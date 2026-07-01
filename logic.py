import storage
import script.pokemons
import script.menus as menus
import team
import os, random, time, sys

def clear():
    os.system('cls')

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
    print(f"A wild {selected.name} has appeared!")
    print(f"ID: {selected.id}, Type: {selected.type}, CP: {selected.CP}")

    while True:
        option1 = input(f"Would you like to catch {selected.name}? (Y/N): ").lower()

        if option1 == "y":
            success = random.randint(0, 1)

            if success == 1:
                clear()
                print(f"Gotcha! {selected.name} was caught!")
                print("Where would you like to store this Pokemon?")
                print("1. Main Team")
                print("2. PC Storage")
                while True:
                    try:
                        option2 = int(input("Select an option: "))

                        if option2 == 1:
                            if team.add_pokemon_team(team_l, selected, PC):
                                print(f"{selected.name} joined your party!")
                            else:
                                print("Your Main Team is full")
                                print(f"{selected.name} was sent to the PC!")
                            break

                        elif option2 == 2:
                            storage.add_pokemon_PC(PC, selected)
                            break

                        else:
                            print("Invalid option.")

                    except ValueError:
                        print("Invalid option.")

                menus.enter_to_continue()

            else:
                clear()
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
                print()
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
                print()
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
                print()
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
            else:
                
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
                    if i.id == option2:
                        if professor_stack.push(i):
                            clear()
                            menus.professor_oak_transfer_title()
                            print("Transfering to professor Oak...")
                            time.sleep(2)
                            clear()
                            menus.professor_oak_transfer_title()
                            print (f"{i.name} was transfered to professor Oak")
                            option3 = input("Cancel Transfer? (Y/N): ")
                            index = team_l.index(i)
                            team_l[index] = None
                            if option3.lower() == "y":
                                popped = professor_stack.pop()
                                index = team.find_none(team_l)
                                team_l[index] = popped
                                print(f"{popped.name} was tranfered back to your Team")
                                break
                            if option3.lower() == "n":
                                break
                            else:
                                print("Invalid Option")
                                print()
                                menus.enter_to_continue()
                        else: 
                            print("professor Oak has 5 Pokemons already")
                            print()
                            menus.enter_to_continue()
                        found == True
                if not found:
                    print(f"Pokemon with {option2} ID was not found")
                    print()
                    menus.enter_to_continue()
                    break

        elif option1 == 2:
            if PC.count_nodes() == 0:
                print("Your PC is empty")
                print()
                menus.enter_to_continue()
            else:
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
                for i in PC.values():
                    if i.id == option2:
                        if professor_stack.push(i):
                            clear()
                            menus.professor_oak_transfer_title()
                            print("Transfering to professor Oak...")
                            time.sleep(2)
                            clear()
                            menus.professor_oak_transfer_title()
                            print (f"{i.name} was transfered to professor Oak")
                            option3 = input("Cancel Transfer? (Y/N): ")
                            PC.delete(i)
                            if option3.lower() == "y":
                                popped = professor_stack.pop()
                                PC.add_node(i)
                                print(f"{popped.name} was tranfered back to your Team")
                                break
                            if option3.lower() == "n":
                                break
                            else:
                                print("Invalid Option")
                                print()
                                menus.enter_to_continue()
                        else: 
                            print("professor Oak has 5 Pokemons already")
                            print()
                            menus.enter_to_continue()
                        found == True
                if not found:
                    print(f"Pokemon with {option2} ID was not found")
                    print()
                    menus.enter_to_continue()

        elif option1 == 3:
            clear()
            menus.professor_oak_transfer_title()
            popped = professor_stack.pop()
            PC.add_node(i)
            print(f"{popped.name} was tranfered back to your PC")
            print()
            menus.enter_to_continue()

        elif option1 == 4:
            break
        else:
            print("Invalid option")
            menus.enter_to_continue()

def undo_last_transfer(professor_stack, PC):
    clear()
    menus.professor_oak_transfer_title()
    popped = professor_stack.pop()
    PC.add_node(popped)
    print(f"{popped.name} was tranfered back to your PC")
    print()
    menus.enter_to_continue()

def challenge_gym_leader(obtained_medals):
    clear()
    success = random.randint(0,1)
    option1 = menus.gym_challenge_menu()
    if success == 1:
        if obtained_medals.put(option1):
            menus.badge_earned_menu(option1)
        else:
            menus.badge_already_owned_menu(option1)
    else:
        menus.badge_not_earned_menu()

def exit():
    clear()
    print("Thanks for playing")
    sys.exit()

def else_():
    print("Invalid option")
    menus.enter_to_continue()