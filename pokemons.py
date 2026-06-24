import json, random
from hash_map_set import HashMap, HashSet
from linked_list import SingleLink

class Pokemon:
    def __init__(self, id, name, type, CP):
        self.id = id
        self.name = name
        self.type = type
        self.CP = CP

def load_pokemons():
    with open('pokedex.json', 'r') as file:
        pokedex = json.load(file)
        size = len(pokedex)

    map = HashMap(size)

    for pokemon in pokedex:
        map.put(pokemon["id"], Pokemon(pokemon["id"], pokemon["name"], pokemon["type"], pokemon["CP"]))
    return map

def load_medals():
    with open("medals.json", "r") as file:
        medals = json.load(file)
        size = len(medals)
    
    set = HashSet(size)

    for medal in medals:
        set.put(medal)
    return set