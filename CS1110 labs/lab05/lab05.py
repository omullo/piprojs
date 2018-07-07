# lab05.py
# Frank Otieno
# PUT DATE YOU COMPLETED HERE
# Skeleton by Walker White (wmw2), Lillian Lee (LJL2), Feb 2018


"""Functions to complete for CS1110 lab on objects and conditionals."""


import timer


def add_timers(timer1, timer2):
    """Returns: A new Timer object representing the sum of the times in
    timer1 and timer2.  Does not alter timer1 or timer2.

    Example: if timer1 represents 1 hr 59 min and timer2 represents 1 hr 2 min,
    then the **new** returned Timer represents 3 hr 1 min.

    Preconditions:
        timer1 is a Timer object
        timer2 is a Timer object"""
     # PLACEHOLDER: REPLACE WITH YOUR IMPLEMENTATION.
          # HINT1: The main challenge is to figure out what to do if the minutes
          #        add up to more than 60.  It's useful to use the remainder
          #        operator `%`; for example, 61 % 60 is 1.  And it's useful
          #        to remember the `//` operator; for example, 61 // 1 is 1.
          # HINT2: The class Timer is defined in module `timer`, which we've
          #        imported above. So, to create a new Timer, you need a
          #        call like timer.Timer(..., ...)
          # HINT3: You can use if/then/elif/else statements if you want.
          
          
    hoursum=timer1.hours+timer2.hours
    minsum=timer1.minutes+timer2.minutes
    if minsum >59 :
      hoursum=hoursum+1
      minsum=minsum %60
              
    t=timer.Timer(hoursum,minsum)
    return t


####### Pig Latin helper functions


# helper for first_vowel; students do not need to use this directly.
def my_find(letter, s):
    """Returns: position of letter in s, or len(s) if letter not in s.
    Intended use is as a helper for first_vowel.

    Precondition: letter is a lowercase letter
        s is a possibly empty string of lowercase letters."""

    # This function is a workaround for the fact that it would be more
    # convenient for us, in this lab, if str.find returned a big
    # number, like len(s),  when it failed, rather than -1.

    found_result = s.find(letter)
    if found_result > -1:
        return found_result
    else:
        return len(s)


# helper for students, who should use it without modification
def first_vowel(w):
    """Returns: position of the first vowel in w, -1 if no vowel,
    where vowels are defined as in the lab handout.

    Precondition: w is a nonempty string with only lowercase letters."""

    # best_location is smallest index found so far of a vowel;
    # it has value len(w) if none found yet
    best_location = len(w)
    best_location = min(best_location, my_find('a', w))
    best_location = min(best_location, my_find('e', w))
    best_location = min(best_location, my_find('i', w))
    best_location = min(best_location, my_find('o', w))
    best_location = min(best_location, my_find('u', w))

    # can only count a y if w has at least one letter in it
    if len(w) > 1:
        best_y_location = 1 + my_find('y', w[1:])
        best_location = min(best_location, best_y_location)

    if best_location < len(w):
        return best_location
    else:
        return -1


def pigify(w):
    """Returns: copy of w converted to Pig Latin according to the lab handout's
    rules.

    Preconditions:
       w is a nonempty string consisting of only lowercase letters.
       If w begins with a 'q', then the next letter is a 'u'.

    """
    # STUDENTS: Use the helper function first_vowel defined above
    # PLACEHOLDER: REPLACE WITH YOUR IMPLEMENTATION
   
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
    
    


         

        

        
    