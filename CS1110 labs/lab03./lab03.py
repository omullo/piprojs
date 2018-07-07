"""
Functions for handling Strings

This module provides a few functions for manipulating strings. This module is intended 
to prepare you for the first assignment.

<Frank Otieno>
<02/16/2017>
"""


def has_a_vowel(s):
    """
    Returns: True if s has at least one vowel (a, e, i, o, or u)
    
    This function does not count y as a vowel.
    
    Parameter s: a string to check
    Precondition: s is a non-empty string
    
    This function may include intentional errors.
    """
    return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s


def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters
    
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.
    
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    # Implement the function here
    m=s[s.index('"')]

