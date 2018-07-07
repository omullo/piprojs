# lab09.py
# FRANK Otieno
# THE DATE COMPLETED HERE
# Skeleton by various CS1110 profs over the years

"""Recursive Functions. See the associated test file for test cases."""

# STUDENTS in CS1110 2018 Spring: due to the A3 and Spring Break schedule,
# you need only have worked on the first two functions in this file to get
# checked off.
#
# However, we strongly recommend that by the time prelim 2 rolls
# around, you have solved all four exercises.

def numberof(thelist, v):
    """Returns: number of times int v occurs in thelist, a possibly empty list of
    ints.  """
    
    if thelist==[]:
        return 0
    elif thelist[0]!=v:
        return numberof(thelist[1:],v)
    elif thelist[:1]==[v]:
        left=1
        right=numberof(thelist[1:],v)
        return left+right
       
def sum_nested_list(theinput):
    """Returns: Summation of all the numbers in the nested list theinput

    Example:
    sum_nested_list([0, [2, 5, []], 8, [-10, -1]]) should be  4

    Precondition: theinput is an integer, or a potentially nested
    list of integers. It is possible for component lists to be empty"""
    

    # Hint: since you want to do something different depending on whether
    # theinput is a list or an int, you'll want to check the result of
    # type(theinput)

    # Note: there are several possible approaches, including using
    # list slicing, using map, or using a for-loop together with recursion.
    summ=0
    if type(theinput)==int:
        return theinput

    
    # if theinput==[]:
    #     return summ
    for ind in theinput:
        if type(ind)==list:
            summ=summ+sum_nested_list(ind)
            
            # return summ
        else:
            summ=summ+ind
             
    return summ
    



#### STUDENTS: below are two exercises you should complete on your own time,
#### but need not be completed by the time you go to check in this lab.


def replace(thelist, a, b):
    """Returns: a COPY of thelist but with all occurrences of int a replaced by
    int b.  Does not change thelist.

        Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Precondition: thelist is a possibly empty list of ints."""
    if thelist==[]:
        return []
    left =thelist[0]
    if left==a:
        thelist[0]=b
    if len(thelist)>2:
        replace(thelist[1:],a,b)
    if len(thelist)==2:
        replace([thelist[1]],a,b)
    return thelist
        
    

def print_nested_list(theinput):
    """Prints out every single string in theinput, one per line, UNLESS
    theinput is a string, in which case it just prints the input.

    Example:
    if theinput is
      [['this'], ['is', ['a', ['very', 'very', 'very'], ['nes ted', 'list']]]]
    then print_nested_list(theinput) should result in the following printout
       this
       is
       a
       very
       very
       very
       nes ted
       list

    Precondition: input is a string, or a potentially nested potentially empty
    list of strings."""
    pass # REPLACE WITH RECURSIVE IMPLEMENTATION. MORE TEST CASES IN lab09_test.py

    # Hint: since you want to do something different depending on whether
    # theinput is a list or a string, you'll want to check the result of
    # type(theinput)

    # Note: there are several approaches that work, including using list
    # slicing, using a for-loop together with recursion, and using map.

