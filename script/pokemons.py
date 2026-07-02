import json, random
from script.hash_map_set import HashMap, HashSet
from script.linked_list import SingleLink

class Pokemon:
    def __init__(self, id, name, type, CP):
        self.id = id
        self.name = name
        self.type = type
        self.CP = CP

def load_pokemons():
    with open('jsons\pokedex.json', 'r') as file:
        pokedex = json.load(file)
        size = len(pokedex)

    map = HashMap(size)

    for pokemon in pokedex:
        map.put(pokemon["id"], Pokemon(pokemon["id"], pokemon["name"], pokemon["type"], pokemon["CP"]))
    return map

def load_medals():
    with open("jsons\_badges.json", "r") as file:
        medals = json.load(file)
        size = len(medals)
    
    set = HashSet(size)

    for medal in medals:
        set.put(medal)
    return set

import random

def preload_medals(medals_set):
    set = HashSet(2)
    medals = list(medals_set.values())
    counter = 0

    while counter != 2:
        selected = random.choice(medals)
        if selected not in set.values():
            set.put(selected)
            counter += 1

    return set

def select_random_pokemon(map):
    return random.choice(map.values())
