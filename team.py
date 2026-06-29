from storage import add_pokemon_PC
import random
import team, script.menus

def create_team():
    team = [None for _ in range(6)]
    return team

def random_team(team, pokedex):
    counter = 0
    while team[len(team)-1] == None:
        selected = random.choice(pokedex.values())
        if selected not in team:
            team[counter] = selected
            counter += 1
    return team

def show_team(team):
    if all(x is None for x in team):
        print("Empty team")
    for i in team:
        if i != None:
            print(
                    "ID:", i.id,
                    "Name:", i.name,
                    "Type:", i.type,
                    "CP:", i.CP,
                )
        else: pass

def is_empty(team):
    return all(x is None for x in team)

def add_pokemon_team(team, pokemon, PC):
    if pokemon not in team:
        index = find_none(team)
        if index is not None:
            team[index] = pokemon
            return True
    else:
        print(f"{pokemon.name} is already in your Team")
        print(f"Moving {pokemon.name} to your PC")
        add_pokemon_PC(PC, pokemon)
        return None

def find_none(team):
    if None in team:
        return team.index(None)
    return None

def search (team, pokemon):
    found = False
    if is_empty(team):
        print("Your Team is empty")
        print()
        script.menus.enter_to_continue()
    else:
        for i in team:
            if (i.name).lower() == pokemon.lower():
                found = True
                index = i
    return found, index
