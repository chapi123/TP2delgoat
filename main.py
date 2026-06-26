import PC_medic
import script.pokemons
import script.menus as menus
import team
import os, random

def clear():
    os.system('cls')
    
class Game:
    def __init__(self):
        self.PC = PC_medic.create_PC()
        self.medic = PC_medic.create_medic()
        self.pokedex = script.pokemons.load_pokemons() 
        self.all_medals = script.pokemons.load_medals()
        self.obtained_medals = script.pokemons.preload_medals(self.all_medals)
        self.team = team.create_team()


    def run(self):
        while True:
            clear()
            option = menus.main_menu()
            #team.random_team(self.team,self.pokedex)
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
                clear()
                team.show_team(self.team)
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
                                        PC_medic.add_pokemon_PC(self.PC, selected)
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
                found = False
                option1 = menus.find_pokemon_menu()
                for i in self.team:
                    if (i.name).lower() == option1:
                        clear()
                        menus.found_pokemon_menu(i)
                        found = True
                if not found:
                    clear()
                    menus.not_found_menu(option1)
                    
            elif option == 12:
                clear()
                print("Thanks for playing")
                break
            else: 
                print("Invalid option")
                menus.enter_to_continue()
            
            

Game().run()