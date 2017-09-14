'''
Created on 24 kwi 2017

@author: Agnieszka Galeza
'''
import random, string

class RandomStringGenerator(object):
    '''
    Generates random string and random phone number
    '''
    
    @staticmethod
    def generate_random_string(length):
        return "selenium " +''.join(random.choice(string.lowercase) for i in range(length))
    
    @staticmethod
    def generate_random_numbers(start_index, stop_index):
        return ''.join(str(random.randint(0,9)) for i in range(start_index,stop_index))

    @staticmethod
    def generate_random_phone_number():
        return str('+48') + RandomStringGenerator.generate_random_numbers(0, 2)
            
    def __init__(self):
        '''
        Constructor
        '''


#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

ile = int(input("Ile liczb wylosowaæ? "))
lista = []  # pusta lista
for i in range(0, ile):
    lista.append(randint(0, 100))
print(lista)

print("Dodawanie elementów na koñcu listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczbê: "))
    lista.append(liczba)
print(lista)

print("Zawartoœæ listy ([indeks] wartoœæ):")
for i, v in enumerate(lista):
    print("[", i, "]", v)

print("Elementy w odwróconym porz¹dku:")
for e in reversed(lista):
    print(e, end=" ")

print()
print("Elementy posortowane rosn¹co:")
for e in sorted(lista):
    print(e, end=" ")

print()
e = int(input("Któr¹ liczbê usun¹æ? "))
lista.remove(e)
print(lista)

print("Wstawianie elementów do listy")
a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w liœcie")
e = int(input("Podaj liczbê: "))
print("Liczba wyst¹pieñ: ")
print(lista.count(e))
print("Indeks pierwszego wyst¹pienia: ")
if lista.count(e):
    print(lista.index(e))
else:
    print("Brak elementu w liœcie")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Czêœæ listy (notacja wycinkowa):")
i, j = eval(input("Podaj indeks pocz¹tkowy i koñcowy oddzielone przecinkiem: "))
print(lista[i:j])

print()
print("Tupla to lista niemodyfikowalna.")
print("Próba zmiany tupli generuje b³¹d:")
tupla = tuple(lista)
tupla[0] = 100
        