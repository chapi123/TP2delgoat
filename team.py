from linked_list import SingleLink

def create_team():
    team = [None for _ in range(6)] 
    return team


def add_pokemon_team(team, pokemon):
    if None not in team:
      for i in team:
          while i is not None:
              pass
          team[i] = pokemon
    else:
        add_pokemon_PC(pokemon)

def create_PC ():
    PC = SingleLink
    return PC

def add_pokemon_PC(PC, pokemon):
    PC.add_node(pokemon)