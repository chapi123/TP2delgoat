import random
import time
import matplotlib.pyplot as plt

def bubble_sort(listt):
    for i in range(len(listt)):
        for i in range(len(listt) - 1):

            x = listt[i]
            y = listt[i + 1]

            if x > y:
                listt[i], listt[i + 1] = listt[i + 1], listt[i]
    return listt

def selection_sort(listt):
    for i in range(len(listt)):
        min_index = i
        for x in range(i + 1, len(listt)):
            if listt[x] < listt[min_index]:
                min_index = x
        listt[i], listt[min_index] = listt[min_index], listt[i]
    return listt

def insertion_sort(listt):
    for i in range(1, len(listt)):
        value = listt[i]
        x = i - 1

        while x >= 0 and value < listt[x]:
            listt[x + 1] = listt[x]
            x -= 1

        listt[x + 1] = value

    return listt

def partition(array, low, high):  # funcion que acomoda elementos alrededor del pivote
    pivot = array[high]           # toma el ultimo elemento como pivote
    i = low - 1                   # indice del elemento menor

    for j in range(low, high):    # recorre el arreglo desde low hasta high-1
        if array[j].CP <= pivot.CP:     # verifica si el elemento es menor o igual al pivote
            i += 1                # aumenta el indice
            array[i], array[j] = array[j], array[i]  # intercambia posiciones

    array[i+1], array[high] = array[high], array[i+1]  # coloca el pivote en su lugar correcto
    return i+1                   # devuelve la posicion del pivote


def quick_sort(array, low=0, high=None):  # funcion principal de quicksort
    if high is None:                     # verifica si high no fue definido
        high = len(array) - 1            # usa el ultimo indice del arreglo

    if low < high:                       # verifica si hay mas de un elemento
        pivot_index = partition(array, low, high)  # obtiene posicion del pivote
        
        quick_sort(array, low, pivot_index-1)       # ordena la parte izquierda
        quick_sort(array, pivot_index+1, high)      # ordena la parte derecha