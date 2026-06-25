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


def add_pokemon_team(team, pokemon):
    if None not in team:
      for i in team:
          while i is not None:
              pass
          team[i] = pokemon
    else:
        add_pokemon_PC(pokemon)

def add_pokemon_PC(PC, pokemon):
    PC.add_node(pokemon)