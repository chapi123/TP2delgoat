from script.linked_list import SingleLink
from script.queue_stack import Queue

def create_PC ():
    PC = SingleLink()
    return PC

def create_medic ():
    medic = Queue()
    return medic

def add_pokemon_PC(PC, pokemon):
    PC.add_node(pokemon)