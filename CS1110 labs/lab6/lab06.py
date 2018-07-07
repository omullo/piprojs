"""
A module for implementing the Lab 06 functions.

This module uses the Time class provided by the module ctime.  It contains two functions 
function: add_time and add_minutes.

While you are encouraged to test your answers, you do not need to write  a unit test.  
Simply demonstrate your functions to you instructor to get get credit

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""
import ctime


def add_time(time1, time2):
    """
    Returns: The sum of time1 and time2 as a new Time object
    
    Example: Sum of 1hr 59min and 1hr 2min is 3hr 1min 
    DO NOT ALTER time1 or time2, even though they are mutable
    
    Parameter time1: the starting time
    Precondition: time1 is a Time object
    
    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    hoursum=time1.hours+time2.hours
    minsum=time1.minutes+time2.minutes
    if minsum >59 :
      hoursum=hoursum+1
      minsum=minsum %60
              
    t=ctime.Time(hoursum,minsum)
    return t


def add_minutes(time, minutes):
    """
    Alters the object time by adding the given number of minutes
    
    This is a PROCEDURE.  It does not return anything.
    
    Example: It time is 1hr 59min and minutes is 20, this function
    alters time so that it is now 2hr 19min.
    
    Parameter time: the starting time
    Precondition: time is a Time object
    
    Parameter minutes: the number of minutes to add to time
    Precondition: minutes is an int >= 0
    """
    
    hours=time.hours
    minutes=time.minutes
    minsum=time.minutes+minutes
    time.minutes=minsum
    print("here")
    if minsum >59 :
        hours=time.hours+1
        minsum= minsum%60
        
        
time=ctime.Time(1,30)





        