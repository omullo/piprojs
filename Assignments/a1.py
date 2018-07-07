"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Frank Otieno foo6
THE DATE COMPLETED HERE
"""

def before_space(s):
    '''Returns: Substring of s; up to, but not including, the first space
    
    Parameter s: the string to slice
    
    Precondition: s has at least one space in it.
    
    '''
    space = s.find(' ')
    pre=s[:space] #characters before the space
    
    return pre # expected value
    
def after_space(s):
        ''' Returns: Substring of s after the first space
        
        Parameter s: the string to slice
        
        Precondition : s has at least one space in it
        
        '''
        space = s.find(' ')
        post=s[space+1:] #characters after the space
        
        return post  # expected response
    
def first_inside_quotes(s):
        ''' Returns: The first substring of s between two (double) quote characters
        
        Parameter s: a string to search
        
        Precondition: s is a string with at least two (double) quote charaters
        
        '''
        before=s.find('"')
        new= s[before+1:]
        
        after=new.find('"')
        
        result=new[:after]
        
        print (result)
        
        return result
    
    
def get_lhs(json):
        
        ''' Returns: The the LHS value in the response to a currency query.
        
        Parameter json: a json string to parse
        Precondition: json is the response to a currency query
        
        '''
        goal=json.index('lhs')
        new = json[goal:]
        colon = new.find(":")
        output = first_inside_quotes(new[colon:])
        
        print (output)
        
        return output
    
def get_rhs(json):
        ''' Returns: The RHS value in the response to a currency query.
        Parameter json: a json string to parse
        Precondition: json is the response to a currency query
        
        '''
        goal=json.index('rhs')
        new=json[goal:]
        colon=new.find(':')
        output=first_inside_quotes(new[colon:])
        
        print(output)
        
        return output
    
def has_error(json):
        ''' Returns: True if the query has an error; False otherwise.
        Parameter json: a json string to parse
        Precondition: json is the response to a currency query
        '''
        coma=json.index(',')
        new=json[:coma]
        if new.find('true')==-1:
            return True
        else:
            return False

import cornell       
def currency_response(currency_from, currency_to, amount_from):
        """
        Returns: a JSON string that is a response to a currency query.
    
        A currency query converts amount_from money in currency currency_from 
        to the currency currency_to. The response should be a string of the form
    
            '{"success":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "error":""}'
    
        where the values old-amount and new-amount contain the value and name for the 
        original and new currencies. If the query is invalid, both old-amount and 
        new-amount will be empty, while "success" will be followed by the value false.
    
        Parameter currency_from: the currency on hand (the LHS)
        Precondition: currency_from is a string
    
        Parameter currency_to: the currency to convert to (the RHS)
        Precondition: currency_to is a string
    
        Parameter amount_from: amount of currency to convert
        Precondition: amount_from is a float
        """
        
        return cornell.urlread('http://cs1110.cs.cornell.edu/2017fa/a1server.php?src=' + currency_from+ '&dst=' +currency_to+'&amt='+str(amount_from))
    
    
def iscurrency(currency):
        """
        Returns: True if currency is a valid (3 letter code for a) currency. 
        It returns False otherwise.

        Parameter currency: the currency code to verify
        Precondition: currency is a string.
        """
        json_string = currency_response(currency, USD, 1.5)
        if has_error(json_string):
            return False
        else:
            return True
        
def exchange(currency_from, currency_to, amount_from):
        '''
        Returns: amount of currency received in the given exchange.
        In this exchange, the user is changing amount_from money in currency
        currency_from to the currency currency_to. The value returned represents the amount in currency currency_to.
        
        The value returned has type float.

        Parameter currency_from: the currency on hand (the LHS)
        Precondition: currency_from is a string for a valid currency code
    
        Parameter currency_to: the currency to convert to (the RHS)
        Precondition: currency_to is a string for a valid currency code
    
        Parameter amount_from: amount of currency to convert
        Precondition: amount_from is a float
        '''
        conversion=currency_response(currency_from, currency_to, amount_from)
        rhs=get_rhs(conversion)
        new_cur=float(before_space(rhs))
        #string_to_float=float(before_space_call)
        return new_cur
