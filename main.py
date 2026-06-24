from PC_medic import create_medic, create_PC
from pokemons import load_medals, load_pokemons
import menus

class Game:
    def __init__(self):
        self.PC = create_PC()
        self.medic = create_medic()
        self.pokedex = load_pokemons()
        self.medals = load_medals()

    def run(self):
        while True:
            opcion = menus.main_menu()
            print(opcion,type(opcion))

            if opcion == 1:
                opcion1 = menus.pokedex_select()
                if opcion1 == 1:
                    for i in self.pokedex:
                        print(self.pokedex[i].id, self.pokedex[i].name, self.pokedex[i].type, self.pokedex[i].PC)

Game().run()