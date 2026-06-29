import storage
import script.pokemons
import script.menus as menus
import team
import os, random, time

def clear():
    os.system('cls')
    
class Game:
    def __init__(self):
        self.PC = storage.create_PC()
        self.center = storage.create_center()
        self.pokedex = script.pokemons.load_pokemons() 
        self.all_medals = script.pokemons.load_medals()
        self.obtained_medals = script.pokemons.preload_medals(self.all_medals)
        self.team = team.create_team()
        self.profesor_stack = storage.create_profesor_stack()


    def run(self):
        while True:
            clear()
            option = menus.main_menu()
            #self.PC.add_node(script.pokemons.select_random_pokemon(self.pokedex))
            
            if option == 1:
                clear()
                option1 = menus.pokedex_select()
                clear()
                if option1 == 1:
                    menus.pokedex_title()
                    for pokemon in self.pokedex.values():
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
                    pokemon = self.pokedex.get(selected)
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
        
            elif option == 2:
                team.random_team(self.team,self.pokedex)
                clear()
                menus.main_team_title()
                team.show_team(self.team)
                print()
                menus.enter_to_continue()

            elif option == 3:
                clear()
                menus.PC_title()
                if self.PC.count_nodes() != 0:
                    self.PC.print_PC_values()  
                else:
                    print("Your PC is Empty")
                print()
                menus.enter_to_continue()

            elif option == 4:
                clear()
                while True:
                    option1 = menus.badges_menu()
                    if option1 == 1:
                        clear()
                        menus.earned_badges_title()
                        counter = 1
                        for i in self.obtained_medals.values():
                            print(f"{counter}. {i}")
                            counter += 1
                        print(f"Progress:{counter-1}/8")
                        print("")
                        menus.enter_to_continue()
                        break
                    elif option1 == 2:
                        clear()
                        menus.all_badges_title()
                        self.all_medals.print_set()
                        print("")
                        menus.enter_to_continue()
                        break
                    else:
                        print("Invalid option")
                        menus.enter_to_continue()
                    

            elif option == 5:
                clear()
                selected = script.pokemons.select_random_pokemon(self.pokedex)
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
                                        if team.add_pokemon_team(self.team, selected, self.PC):
                                            print(f"{selected.name} joined your party!")
                                        else:
                                            print("Your Main Team is full")
                                            print(f"{selected.name} was sent to the PC!")
                                        break

                                    elif option2 == 2:
                                        storage.add_pokemon_PC(self.PC, selected)
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
            
            elif option == 6:
                clear()
                if self.PC.count_nodes() != 0:
                    while True:
                        option1 = menus.sorting_PC_menu()
                        if option1 == 1:
                            clear()
                            menus.sorting_PC_title()
                            self.PC.bubble_sort()
                            print()
                            print("PC has been sorted alphabetically")
                            print()
                            self.PC.print_PC_values()
                            print()
                            menus.enter_to_continue()
                            break
                        elif option1 == 2:
                            clear()
                            menus.sorting_PC_title()
                            self.PC.insertion_sort()
                            print()
                            print("PC has been sorted by Type")
                            print()
                            self.PC.print_PC_values()
                            print()
                            menus.enter_to_continue()
                            break
                        elif option1 == 3:
                            clear()
                            menus.sorting_PC_title()
                            self.PC.quick_sort_nodes()
                            print()
                            print("PC has been sorted by CP")
                            print()
                            self.PC.print_PC_values()
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

            elif option == 7:
                clear()
                option1 = menus.find_pokemon_menu()
                found, index = team.search(self.team, option1)

                if found:
                    clear()
                    menus.found_pokemon_menu(index)
                else:
                    clear()
                    menus.not_found_menu(option1)
            
            elif option == 8:
                if not team.is_empty(self.team):
                    clear()
                    while True:
                        option1 = menus.pokemon_center_menu()
                        if option1 == 1:
                            clear()
                            menus.pokemon_center_title()
                            print("Healing your Pokemons...")
                            for i in self.team:
                                self.center.enqueue(i)
                            for i in self.center.values():
                                clear()
                                menus.pokemon_center_title()
                                healed = self.center.dequeue()
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

            elif option == 9:
                clear()
                while True:
                    option1 = menus.profesor_oak_transfer_menu()
                    if option1 == 1:
                        clear()
                        menus.professor_oak_transfer_title()
                        if team.is_empty(self.team):
                            print("Your Team is empty")
                            print()
                            menus.enter_to_continue()
                        else:
                            
                            while True:
                                try:
                                    menus.professor_oak_transfer_title()
                                    team.show_team(self.team)
                                    print()
                                    option2 = int(input("Select a Pokemon's ID: "))
                                    break
                                except:
                                    print("Invalid option")
                                    print()
                                    menus.enter_to_continue()

                            for i in self.team:
                                if i.id == option2:
                                    if self.profesor_stack.push(i):
                                        clear()
                                        menus.professor_oak_transfer_title()
                                        print("Transfering to Profesor Oak...")
                                        time.sleep(2)
                                        clear()
                                        menus.professor_oak_transfer_title()
                                        print (f"{i.name} was transfered to profesor Oak")
                                        option3 = input("Cancel Transfer? (Y/N): ")
                                        index = self.team.index(i)
                                        self.team[index] = None
                                        if option3.lower() == "y":
                                            popped = self.profesor_stack.pop()
                                            index = team.find_none(self.team)
                                            self.team[index] = popped
                                            print(f"{popped.name} was tranfered back to your Team")
                                            break
                                        if option3.lower() == "n":
                                            break
                                        else:
                                            print("Invalid Option")
                                            print()
                                            menus.enter_to_continue()

                    elif option1 == 2:
                        if self.PC.count_nodes() == 0:
                            print("Your PC is empty")
                            print()
                            menus.enter_to_continue()
                        else:
                            pass
                    elif option1 == 3:
                        pass
                    elif option1 == 4:
                        break
                    else: pass


            elif option == 12:
                clear()
                print("Thanks for playing")
                break
            else: 
                print("Invalid option")
                menus.enter_to_continue()
            
            

Game().run()