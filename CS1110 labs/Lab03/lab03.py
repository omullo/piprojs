# lab03.py
# Frank otieno foo6
# 02/14/2018
# Skeleton by Walker M. White (wmw2), Lillian Lee (LJL2), Feb 2018


""" Contains a useful string function.

CAVEATS:

This module is distributed for the purposes of exercising testing and
debugging. Hence, be aware that, as originally written, the implementation of
the useful string function may contain conceptual errors.
"""


def replace_first(word,target,rep):
    """Returns: a copy of string `word` with the FIRST instance of string
    `target` in `word` replaced by string `rep`

    Example: replace_first('methos', 's', 'd') -> 'method'

    Precondition: `target` has length >=1 and appears in `word`

    """
    pos = word.index(target)  # where the first target starts
    
    print("DEBUG: pos is: " + str(pos))

    before = word[:pos]  # part of word up to but not including first target
    
    print("DEBUG: before is:" +str(before))

    after = word[pos+len(target):]  # part of word after target
    
    print("DEBUG: after is: " +str(after))

    result = before + rep + after  # desired output
    
    print("DEBUG: result is:" +str(result))
    
    return result
