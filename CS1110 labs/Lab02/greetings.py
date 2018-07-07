# greetings.py
# Frank Omullo foo6
# Feb, 2018
# Skeleton by Prof Lillian Lee

"""Library of functions producing greetings"""
import random

def multi_hi(name,num):
    """Returns a string of the form: "hi " repeated <num> times, followed by
    <name>, followed by "!".
    Preconditions (i.e., assumptions this function makes about its input):
        name is a string
        num is a positive int
        """    
    return "hi "*num + name + "!"


def rand_hi(name):
    """SEE LAB HANDOUT.
    Precondition: name is a string"""
    reps = random.randint(1,6)# ***placeholder: replace as instructed***
    return multi_hi(name,reps)
    

def natural_hi():
    """SEE LAB HANDOUT"""
    input_name = input('Please enter your name: ')
    return rand_hi(input_name)