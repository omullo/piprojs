#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:05:46 2018

@author: frank
"""

# loop_invariants_worked_examples.py
# D. Gries, L. Lee, S. Marschner, W. White
# Apr 7, 2013

"""Code accompanying the reading "CS1110: Worked examples regarding loops and
invariants", with ASCII-art visualization"""

import inspect


def _whoami():
    """Returns: name of function it is called in"""
    return inspect.stack()[1][3]


def printindex(varchar, position, lastspot):
    """Print a line where character <varchar>, meant to be an index variable,
    is at space <position>, with <position>-1 periods preceding it, and with
    periods following it up to position <lastspot>.
    Precond: <lastspot> + 1 >= <position>, <position> >= 0."""
    spacing = ''  # preceding dots
    for s in range(lastspot+1):
        if s == position:
            spacing += varchar
        else:
            spacing += '.'
    if position == lastspot + 1:
        spacing += varchar
    print (spacing)


def printlist(b):
    """Print the contents of the list, with no separators"""
    out = ''  # progress towards output
    for item in b:
        out = out + str(item)
    print (out)


def minp1(b, h, k, verbose=False):
    """Returns an int i such that b[i] is the minimum value in b[h..k].
    Pre: 0 <= h <= k < len(b). If verbose, also prints out incremental
    output showing the internal state of variables at each loop iteration.

    Uses invariant P1 from the reading.
    """
    # Inv says b[t+1..k] are '???'. Start: b[h+1..k] '???'.
    # End: b[k+1..k] '???'.

    def printinfo():
        """Local function; print internal state"""
        printindex('k',k,len(b)-1)
        printindex('h',h, len(b)-1)
        printindex('t',t, len(b)-1)
        printindex('i',i, len(b)-1)
        printlist(b); print ('\n')

    i = h; t = h
    if verbose:
        printinfo()
    while (t < k):   # still have '???' to process
        # peek at next '???'
        if b[t+1] < b[i]:
            i = t+1  # location of smaller value
            t = t+1  # update knowledge, progress towards termination
        else:  # the next unknown is at least as big as the known min
            t = t+1  # update knowledge, progress towards termination
        if verbose:
            printinfo()
    if verbose:
        print ('done with ' + _whoami() + ' loop\n')
    return i


def minp2(b, h, k, verbose=False):
    """Returns an int i such that b[i] is the minimum value in b[h..k].
    Pre: 0 <= h <= k < len(b). If verbose, also prints out incremental
    output showing the internal state of variables at each loop iteration.

    Uses invariant P2 from the reading.
    """
    # Inv says b[s..k] are '???'. Start: b[h+1..k] '???'.
    # End: b[k+1..k] '???'.

    def printinfo():
        """Local function; print internal state"""
        printindex('k',k,len(b)-1)
        printindex('h',h, len(b)-1)
        printindex('s',s, len(b)-1)
        printindex('i',i, len(b)-1)
        printlist(b); print ('\n')

    i = h; s = h+1
    if verbose:
        printinfo()
    while (s < k+1):   # still have '???' to process
        # peek at next '???'
        if b[s] < b[i]:
            i = s # location of smaller value
            s = s+1  # update knowledge, progress towards termination
        else:  # the next unknown is at least as big as the known min
            s = s+1  # update knowledge, progress towards termination
        if verbose:
            printinfo()
    if verbose:
        print ('done with ' + _whoami() + ' loop\n')
    return i


def minp3(b, h, k, verbose=False):
    """Returns an int i such that b[i] is the minimum value in b[h..k].
    Pre: 0 <= h <= k < len(b). If verbose, also prints out incremental
    output showing the internal state of variables at each loop iteration.

    Uses invariant P3 from the reading.
    """
    # Inv says b[h..r-1] are '???'. Start: b[h..k-1] '???'.
    # End: b[h..h-1] '???'.

    def printinfo():
        """Local function; print internal state"""
        printindex('k',k,len(b)-1)
        printindex('h',h, len(b)-1)
        printindex('r',r, len(b)-1)
        printindex('i',i, len(b)-1)
        printlist(b); print ('\n')

    i = k; r = k
    if verbose:
        printinfo()
    while (r > h):   # still have '???' to process
        # peek at next '???'
        if b[r-1] < b[i]:
            i = r-1 # location of smaller value
            r = r-1  # update knowledge, progress towards termination
        else:  # the next unknown is at least as big as the known min
            r = r-1  # update knowledge, progress towards termination
        if verbose:
            printinfo()
    if verbose:
        print ('done with ' + _whoami() + ' loop\n')
    return i


def part3dot1(b, verbose=False):
    """Rearrange b and return int k so that b[0..k] <= 6 and b[k+1] > 6.
    Pre: b is a list of ints.

    Uses invariant P3.1 from the reading."""

    def printinfo():
        """Local function; print internal state"""
        printindex('h',h, len(b)-1)
        printindex('k',k,len(b)-1)
        printlist(b); print ('\n')

    # Inv says b[h+1..k] are '?'. Start: b[0..len(b)-1] '?'; end: b[h+1..h] '?'.
    h = -1; k = len(b)-1
    if verbose:
        printinfo()
    while k > h: # still have '?' to process
        # peek at next '?'
        if b[h+1] <= 6:
            h = h+1 # update knowledge, progress towards termination
        else:
            b[h+1], b[k] = b[k], b[h+1] # swap to put big val with right-hand brethren
            k = k-1 # update knowledge, progress towards termination
        if verbose:
            printinfo()
    if verbose:
        print ('done with ' + _whoami() + ' loop\n')
    return k


def part4dot1(b, h, k,  verbose=False):
    """Let x = b[h] be the pivot value. Rearrange b[h..k] and return int j so
    that b[0..j-1] <= b[j] <=b[j+1].
    Pre: b is a list of ints, 0 <= h <= k < len(b).

    Uses invariant P4.1 from the reading."""

    def printinfo():
        """Local function; print internal state"""
        printindex('h',h, len(b)-1)
        printindex('k',k,len(b)-1)
        printindex('j', j, len(b)-1)
        printindex('q', q, len(b)-1)
        printlist(b); print ('\n')

    # Inv:  b[j] is pivot, b[j+1..q] '?'. Start: b[h+1..k] '?'; end: b[j+1..j] '?'.
    j=h; q=k
    if verbose:
        printinfo()
    while q > j: # still have '?' to process
        # peek at next '?'
        if b[j+1] <= b[j]:
            b[j+1], b[j] = b[j], b[j+1]
            j = j+1 # pivot value has moved
        else:
            b[j+1], b[q] = b[q], b[j+1] # swap to put big val with right-hand brethren
            q = q-1 # update knowledge, progress towards termination
        if verbose:
            printinfo()
    if verbose:
        print ('done with ' + _whoami() + ' loop\n')
    return j


if __name__ == '__main__':
    # Change the verbose settings to False if you don't want the 'animation'
    list0 = [1,5,5,2,9,7,8]
    lists = [list0,
             [1,2],
             [1,5,5,2,1,7,1]]
    for j in range(len(lists)):
        for fn in [minp1,minp2,minp3]:
            cl = lists[j][:]  # copy of current list, for short
            end = len(cl)-1  # last position in list in question
            assert min(cl[1:end+1]) == cl[fn(cl,1,end,verbose=True)], 'error with list ' + str(j)

    lists.append([])
    for j in range(len(lists)):
        cl = lists[j][:]  # copy of current list
        for fn in [part3dot1]:
            k = fn(cl, verbose=True)
            for m in range(k+1):
                assert cl[m] <=6, 'lefthand partition wrong, list ' + str(j)
            for m in range(k+1,len(cl)):
                assert cl[m] > 6, 'righthand partition wrong, list ' + str(j)

    # test partition
    list1 = [4, 6, 1, 5, 0, 7, 3, 1, 4, 9, 0]
    list2 = [5,8,7,5,7,6,4,0,7]
    lists = [list1, list2, [7,1], [7,8]]

    for n in range(len(lists)):
        for h in [0,1]:
            cl = lists[n][:] # copy of current list, for short
            j = part4dot1(cl,h,len(cl)-1, verbose=True)
            assert cl[j] == lists[n][h]
            for k in range(h,j):  # verify first partition range
                assert cl[k] <= cl[j], 'lefthand partition wrong, list ' + str(j)
            for k in range(j+1, len(cl)):  # verify second partition range
                assert cl[k] >= cl[j], 'righthand partition wrong, list ' + str(j)

    print ('application code for loop invariants completed with no assert errors')
