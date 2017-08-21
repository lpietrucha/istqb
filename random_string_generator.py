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
        