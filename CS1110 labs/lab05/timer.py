# timer.py
# Lillian Lee (LJL2) and Walker White (WMW2)
# Feb 2018

""" Timer class for lab05

Students do not need to edit or even examine this file.

"""


class Timer(object):

    """Instances represent a timer with a resolution of minutes.

    Attributes:
        hours [non-negative int]: number of hours
        minutes [int in the range 0..59]: number of minutes

    """

    ## STUDENTS: don't worry about the syntax of this method definition.
    ## Just know that a call of the form Timer(x,y) will set the new Timer's
    ## hours to x and the Timer's minutes to y.
    def __init__(self, h, m):
        """Sets this Timer's hours to h and minutes to m.

        Preconditions: h is a positive int, h is an int in range 0..59"""
        self.hours = h
        self.minutes = m


import timer
t = Timer(2,30)
# This is like grouping two students on CMS, so that their deadlines are linked
s=t
t.minutes = 20
print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes) + '\n')
# This is like un-grouping the two students on CMS, so their deadlines are
# now no longer linked, even if they have the same values.
s = Timer(t.hours, t.minutes)
print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes) + '\n')
t.minutes = 10
print("t.minutes is: " + str(t.minutes))
print("s.minutes is: " + str(s.minutes))