"""
Module for implementing Lab 05 functions.

This module is broken up into to parts.  The first part contains two
functions: first_vowel and pigify. The first is a helper function of 
the second (which is the primary function). The second function, pigify,
convert English words to Pig-Latin. You are to IMPLEMENT the second function.

The second part requires that you write functions on lists. The functions
may or may not require for loops to be implemented properly.

While you are encouraged to test your answers, you do not need to write 
a unit test.  Simply demonstrate your functions to you instructor to get
get credit

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


# PART 1: Pig Latin

def first_vowel(w):
    """
    Returns: position of the first vowel; -1 if no vowels.
    
    There is a better way to do this function with for-loops, 
    but we have not covered that topic yet.
    
    Parameter w: the string to search
    Precondition: w is a nonempty string with only lowercase letters
    """
    minpos = len(w) # invalid position; currently no vowels found
    
    # search for a
    pos = w.find('a')
    if pos != -1 and pos < minpos: # a found and is closest
        minpos = pos
    
    # search for e
    pos = w.find('e')
    if pos != -1 and pos < minpos: # e found and is closest
        minpos = pos
    
    # search for i
    pos = w.find('i')
    if pos != -1 and pos < minpos: # i found and is closest
        minpos = pos
    
    # search for o
    pos = w.find('o')
    if pos != -1 and pos < minpos: # o found and is closest
        minpos = pos
    
    # search for u
    pos = w.find('u')
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos
    
    # search for y not at front
    pos = w.find('y',1)
    if pos != -1 and pos < minpos: # u found and is closest
        minpos = pos
    
    # found something if minpos moved from first assignment
    return minpos if minpos != len(w) else -1


def pigify(w):
    """
    Returns: copy of w converted to Pig Latin
    
    See the lab handout for the complete rules on Pig Latin.
    
    Parameter w: the word to turn into Pig Latin
    Precondition: w is a nonempty string with only lowercase letters
    """
     if w[0] in 'a e i o u':
        new_w= w+'hay'
        return new_w
    elif w[0]=='q':
        new_word=w[2:]+'qu'+'ay'
        return new_word
    else:
        pos=first_vowel(w)
        if pos==-1:
            new_word=w+'ay'
            return new_word
        else:
            new_word=w[pos:]+w[:pos]+'ay'
            return new_word


# PART 2: Lists

def lesser_than(thelist,value):
    """
    Returns:  number of elements in thelist strictly less than value,
    without altering thelist.
    
    Example: lesser than([5, 9, 1, 7], 6) evaluates to 2
    
    Parameter thelist: the list to search
    Precondition:  thelist is a list of ints
    
    Parameter value: the value to search for
    Precondition: value is an int
    """
    pass # STUB. Implement me


def unique(thelist):
    """
    Returns: The number of unique elements in the list. 
    
    Example: is uniform([5, 9, 5, 7]) evaluates to 3
    Example: is uniform([5, 5, 1, 'a', 5, 'a']) evaluates to 3
    
    HINT: What if you made a second list.  How can you
    be sure the second list has no duplicates?
    
    Parameter thelist: the list to search
    Precondition:  thelist is a list of any values.
    """
    pass # STUB. Implement me
