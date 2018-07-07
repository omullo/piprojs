# a1.py
# Andrew Nkubito and Frank Otieno 
# Sources/people consulted: FILL IN OR WRITE "NONE"
# 03/05/2018
# Skeleton by Prof. Lee (cs1110-prof@cornell.edu), Feb 14 2018

"""
Functions for finding whether a class is open or closed on a roster.

We use "backwards single quotes" --- like this: `hi there` --- in the
docstrings below to visually set off variable names.
"""


# Helper function
def before_first_double_quote(text):
    """Returns: the part of string `text` right up to but not including
    the first double-quote.

    Precondition: string `text` contains at least one double-quote.

    Example: before_first_double_quote('abd"def') returns the string
        abd
    """
    before=text[:text.find('"')]
    
    return before
    


# Helper function
def after(tag, text):
    """Returns: all of string `text` that occurs just after the first
    occurrence of string `tag` in `text`.

    Preconditions:
        `text` [str] contains an instance of `tag`
        `tag` [str] has length > 0

    Example: if `tag` is the string
        <<a <id="c111">
    and `s` is the string
        start <a id="c111">xthis that the other
    then this functions returns the string
         xthis that the other
    """
    post=text[text.find(tag)+len(tag):]
    
    return post


def open_status(class_num, data):
    """Returns the open-ness status of class `class_num` according to `data`.

    `class_num`: string version of a class number, e.g., "10776" at Cornell.

    `data`: a string whose preconditions are easiest explained by example.
        Suppose `class_num` is "10775".
        Then, `data` must contain somewhere within it a single occurrence of
           <a id="c10775">
        and this is followed by text where the first occurrence of the string
            open-status-
        (the ending hyphen is important) is one of
            open-status-open"
        or
            open-status-closed"
        or any string of the form
            open-status-???"
        (the ending double-quote is important to notice)
        where the ??? stands for a sequence of characters not containing quotes
        that represents the open-ness status of the course. (For example, maybe
        there is such a thing as open-status-waitlist")

    This function returns whatever ??? is.

    Example: if `class_num` is "10775", and `data` is the string
        <a id="c10775"> fa-circle open-status-open"></i></span>
    then this function returns the string
        open

    Example: if `class_num` is "10775", and `data` is the string
        dum dee dum <a id="c10775"> open-stat open-status-CLOSED" tral la la
    then this function returns the string
        CLOSED

    Example: if `class_num` is "432" and `data` is the string
        <a id="c4321"> ha open-status-open" <a id="c432"> open-status-never!""
    then this function returns the string
        never!
    (The exclamation point must be included.)

    Example: if `class_num` is "432" and `data` is the string
        <a  id="c432"> ho open-status-open" <a id="c432"> open-status-nope."
    then this function returns the string
        nope.
    (The number of spaces matters between the `a` and the `id` matters.)



    """
   
    m= '<a id="c'+ class_num+ '">'
    p=len(m)
    ki=data.find(m)
    ski=data[ki:p+ki]
    
    grr=after(ski,data)
    
    sor=grr.find('open-status-')
    pk=len('open-status-')
    pik=grr[sor:pk+sor]
    now=after(pik,grr)
    here=before_first_double_quote(now)
   
    
    return here
    
    



def label(class_num, data):
    """Returns, as a single string,  the common name, component and component
    number for class `class_num` according to `data`.

    `class_num`: string version of a class number, e.g., "10776" at Cornell.

    `data`: a string whose preconditions are easiest explained by example.
        Suppose `class_num` is "10782".
        Then, `data` matches the pattern
             ... <a id="c10782"> ... class="course-repeater">CS 1110&nbsp;...
            data-ssr-component="DIS" data-section="208"
        And the function should return the string
            CS 1110 DIS 208
        with no beginning or trailing whitespace.

        That is, `data` must contain somewhere within it a single occurrence of
            <a id="c10782">
        and this is followed by text where the first occurrence of the string
            class="course-repeater">
        (the ending quote and angle-bracket is important) is followed by the
        common name of the course, and then the string
            &nbsp;
        and the first occurrence of the string
            data-ssr-component="
        is followed by the component, followed by a double-quote,
        and the first occurrence of the string
            data-section="
        is followed by the component number followed by a double-quote.

        The function returns the string formed by concatenating the common
        name, then a space, then the component, then a space, then the
        component number.

    """
    m1=('<a id="c'+ class_num+ '">')
    p1= len(m1)
    k1=data.find(m1)
    sk1=data[k1:p1+k1]
    grr1=after(sk1,data)
    
    
    b1=('class="course-repeater">')
    q=len(b1)
    q1=grr1.find(b1)
    sq1=grr1[q1:q+q1]
    grr2=after(sq1,grr1)
    bu=grr2.find('&')
    kp=grr2[:bu] #kp is the name of the class.
    
    a=('data-ssr-component="')
    a1=len(a)
    a3=grr1.find(a)
    a4=grr1[a3:a1+a3]
    a5=after(a4,grr1)
    a6=before_first_double_quote(a5)  #a6 is the name of the data component
    
    c1=('data-section="')
    c2=len(c1)
    c3=a5.find(c1)
    c4=a5[c3:c3+c2]
    c5=after(c4,a5)
    c6=before_first_double_quote(c5) # c6 is the name of the data section
    goal=(kp+' '+a6+' '+c6) #concatenated output.
   
    return goal

    
    



