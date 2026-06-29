from script.linked_list import SingleLink
from script.queue_stack import Queue, Stack

def create_PC ():
    PC = SingleLink()
    return PC

def create_center ():
    center = Queue()
    return center

def add_pokemon_PC(PC, pokemon):
    PC.add_node(pokemon)

def create_profesor_stack():
    stack = Stack()
    return stack