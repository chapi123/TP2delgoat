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
            
            if option == 1:
                clear()
                option1 = menus.pokedex_select()
                clear()
                if option1 == 1:
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
                if self.PC.count_nodes() != 0:
                    if self.PC.head:
                        current = self.PC.head
                        if current == None:
                            return None
                        while current != None:
                            print(
                                "ID:", current.data.id,
                                "Name:", current.data.name,
                                "Type:", current.data.type,
                                "CP:", current.data.CP,
                            )
                            current = current.next
                    else: return None   
                else:
                    print("Empty PC")
                menus.enter_to_continue()

            elif option == 4:
                clear()
                print("Obtained medals:")
                counter = 1
                for i in self.obtained_medals.values():
                    print(f"{counter}. {i}")
                    counter += 1
                menus.enter_to_continue()

            elif option == 5:
                clear()
                selected = script.pokemons.select_random_pokemon(self.pokedex)
                print(f"A wild {selected.name} has appeared!")
                print(f"ID: {selected.id}, Type: {selected.type}, CP: {selected.CP}")
                option1 = input(f"Would you like to catch {selected.name}? (Y/N): ")
                if option1.lower() == "y":
                    success = random.randint(0,1)
                    if success == 1:
                        clear()
                        print(f"Gotcha! {selected.name} was caught!")
                        print("Where would you like to store this Pokemon?")
                        print("1. Main Team")
                        print("2. PC Storage")
                        option2 = int(input("Select an option: "))
                        if option2 == 1:
                            if team.add_pokemon_team(self.team, selected, self.PC):
                                print(f"{selected.name} joined your party!")
                            else:
                                print("Your Main Team is full")
                                print(f"{selected.name} was sent to the PC!")
                            menus.enter_to_continue()
                        elif option2 == 2:
                            PC_medic.add_pokemon_PC(self.PC, selected)
                        else:
                            print("Invalid option")
                            menus.enter_to_continue()
                    if success == 0:
                        clear()
                        print(f"Oh no! {selected.name} escaped!")
                        menus.enter_to_continue()
                elif option1.lower() == "n":
                    pass
                else:
                    print("Invalid option")
                    menus.enter_to_continue()

            elif option == 11:
                clear()
                print("Thanks for playing")
                break
            else: 
                print("Invalid option")
                menus.enter_to_continue()
            
            

Game().run()