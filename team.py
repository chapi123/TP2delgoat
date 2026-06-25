from PC_medic import add_pokemon_PC

def create_team():
    team = [None for _ in range(6)]
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
    index = find_none(team)
    if index is not None:
          team[index] = pokemon
          return True
    else:
        add_pokemon_PC(PC, pokemon)
        return None

def find_none(team):
    if None in team:
        return team.index(None)
    return None