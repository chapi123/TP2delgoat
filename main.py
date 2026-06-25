from PC_medic import create_medic, create_PC
from script.pokemons import load_medals, load_pokemons
import script.menus as menus
import team
import os

def clear():
    os.system('cls')
    
class Game:
    def __init__(self):
        self.PC = create_PC()
        self.medic = create_medic()
        self.pokedex = load_pokemons()
        self.medals = load_medals()
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

            elif option == 11:
                clear()
                print("Thanks for playing")
                break
            else: 
                print("Invalid option")
                menus.enter_to_continue()
            
            



Game().run()