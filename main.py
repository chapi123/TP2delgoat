from PC_medic import create_medic, create_PC
from pokemons import load_medals, load_pokemons

class Game:
    def __init__(self):
        self.PC = create_PC()
        self.medic = create_medic()
        self.pokedex = load_pokemons()
        self.medals = load_medals()

    def print_menu(self):
        print("\n" + "=" * 55)
        print("                    HUERGO POKEMON")
        print("=" * 55)
        print(" 1. Ver Pokédex")
        print(" 2. Ver Equipo Principal")
        print(" 3. Ver PC")
        print(" 4. Capturar nuevo Pokémon")
        print(" 5. Ordenar PC")
        print(" 6. Buscar Pokémon en Equipo")
        print(" 7. Enviar Pokémon al Centro Pokémon")
        print(" 8. Transferir Pokémon al Profesor Oak")
        print(" 9. Deshacer última transferencia")
        print("10. Desafiar Líder de Gimnasio")
        print("11. Salir del sistema")
        print("=" * 55)

        opcion = input("Seleccione una opción: ")
        return opcion

Game().print_menu()