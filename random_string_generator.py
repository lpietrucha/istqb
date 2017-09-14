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

ile = int(input("Ile liczb wylosowa�? "))
lista = []  # pusta lista
for i in range(0, ile):
    lista.append(randint(0, 100))
print(lista)

print("Dodawanie element�w na ko�cu listy")
for i in range(0, 3):
    liczba = int(input("Podaj liczb�: "))
    lista.append(liczba)
print(lista)

print("Zawarto�� listy ([indeks] warto��):")
for i, v in enumerate(lista):
    print("[", i, "]", v)

print("Elementy w odwr�conym porz�dku:")
for e in reversed(lista):
    print(e, end=" ")

print()
print("Elementy posortowane rosn�co:")
for e in sorted(lista):
    print(e, end=" ")

print()
e = int(input("Kt�r� liczb� usun��? "))
lista.remove(e)
print(lista)

print("Wstawianie element�w do listy")
a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))
lista.insert(i, a)
print(lista)

print("Wyszukiwanie i zliczanie elementu w li�cie")
e = int(input("Podaj liczb�: "))
print("Liczba wyst�pie�: ")
print(lista.count(e))
print("Indeks pierwszego wyst�pienia: ")
if lista.count(e):
    print(lista.index(e))
else:
    print("Brak elementu w li�cie")

print("Pobieramy ostatni element z listy: ")
print(lista.pop())
print(lista)

print("Cz�� listy (notacja wycinkowa):")
i, j = eval(input("Podaj indeks pocz�tkowy i ko�cowy oddzielone przecinkiem: "))
print(lista[i:j])

print()
print("Tupla to lista niemodyfikowalna.")
print("Pr�ba zmiany tupli generuje b��d:")
tupla = tuple(lista)
tupla[0] = 100
        