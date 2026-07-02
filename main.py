import storage
import script.pokemons
import script.menus as menus
import team
import os, random
import logic
    

class Game:
    def __init__(self):
        self.PC = storage.create_PC()
        self.center = storage.create_center()
        self.pokedex = script.pokemons.load_pokemons() 
        self.all_medals = script.pokemons.load_medals()
        self.obtained_medals = script.pokemons.preload_medals(self.all_medals)
        self.team = team.create_team()
        self.professor_stack = storage.create_professor_stack()


    def run(self):
        while True:
            logic.clear()
            option = menus.main_menu()
            
            if option == 1:
                logic.view_pokedex(self.pokedex)
        
            elif option == 2:
                logic.view_main_team(self.team, self.pokedex)

            elif option == 3:
                logic.view_PC(self.PC)

            elif option == 4:
                logic.view_medals(self.obtained_medals, self.all_medals)

            elif option == 5:
                logic.capture_new_pokemon(self.pokedex, self.PC, self.team)
            
            elif option == 6:
                logic.sort_PC(self.PC)

            elif option == 7:
                logic.search_pokemon_in_team(self.team)

            elif option == 8:
                logic.send_pokemon_to_pokemon_center(self.team, self.center)

            elif option == 9:
                logic.transfer_pokemon_to_professor_oak(self.team, self.PC, self.professor_stack)

            elif option == 10:
                logic.undo_last_transfer(self.professor_stack, self.PC)

            elif option == 11:
                logic.challenge_gym_leader(self.obtained_medals, self.team)

            elif option == 12:
                logic.manage_team(self.team, self.PC)

            elif option == 13:
                logic.exit()
            else: 
                logic.else_()
            

Game().run()