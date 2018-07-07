"""
Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Frank Otieno foo6
THE DATE COMPLETED HERE
"""
import sys
sys.path.append('/Library/Python/3.6/site-packages')
import cornell

import a1

def testA():
     """Test procedure for Part A"""
     result=a1.before_space('0.12345 Bitcoins')
     cornell.assert_equals('0.12345', result)
     result=a1.before_space('1799.3186929883  Lebanese Pounds')
     cornell.assert_equals('1799.3186929883', result)
     result=a1.before_space('7.725799   Solomon Islands Dollars')
     cornell.assert_equals('7.725799', result)
     result=a1.before_space('1 United States Dollar')
     cornell.assert_equals('1', result)
     result=a1.before_space(' 1 United States Dollar')
     cornell.assert_equals('', result)
     
     result=a1.after_space('0.12345 Bitcoins')
     cornell.assert_equals('Bitcoins', result)
     result=a1.after_space('1799.3186929883 Lebanese Pounds')
     cornell.assert_equals('Lebanese Pounds', result)
     result=a1.after_space('7.725799 Solomon Islands Dollars')
     cornell.assert_equals('Solomon Islands Dollars', result)
     result=a1.after_space('73.8118685829172 Papua New Guinean Kina')
     cornell.assert_equals('Papua New Guinean Kina', result)
     result=a1.after_space('8.0307256337289 Trinidad and Tobago Dollars')
     cornell.assert_equals('Trinidad and Tobago Dollars', result)
     result=a1.after_space('124 Euros ')
     cornell.assert_equals('Euros ', result)
     result=a1.after_space(' 34.5827 Namibian Dollars')
     cornell.assert_equals('34.5827 Namibian Dollars', result)
     result=a1.after_space('17.8686  Mexican Pesos')
     cornell.assert_equals(' Mexican Pesos', result)
     
     #Test for first_inside_quotes
     result=a1.first_inside_quotes('ab"cd"ef')
     cornell.assert_equals('cd',result)
     result=a1.first_inside_quotes('""')
     cornell.assert_equals('',result)
     result=a1.first_inside_quotes('"This is assignment 1"')
     cornell.assert_equals('This is assignment 1',result)
     result=a1.first_inside_quotes('ab"cd"ef"gh"')
     cornell.assert_equals('cd',result)
    
def testB():
     """Test procedure for Part B"""
     result=a1.get_lhs('{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}')
     cornell.assert_equals('2 United States Dollars',result)
     result=a1.get_lhs('{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}')
     cornell.assert_equals('',result)
       
     result=a1.get_rhs('{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}')
     cornell.assert_equals('1.825936 Euros',result)
     result=a1.get_rhs('{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}')
     cornell.assert_equals('',result)
     
     result=a1.has_error('{"success":false, "lhs":"", "rhs":"", "error":"Source currency code is invalid."}')
     cornell.assert_equals(True,result)
     result=a1.has_error('{"success":true, "lhs":"2 United States Dollars", "rhs":"1.825936 Euros", "error":""}')
     cornell.assert_equals(False,result)
    
def testC():
     """Test procedure for Part C"""
     result=a1.currency_response('USD', 'EUR', 2.5)
     cornell.assert_equals('{ "success" : true, "lhs" : "2.5 United States Dollars", "rhs" : "2.0952375 Euros", "error" : "" }',result)
     result=a1.currency_response('p', 'EUR', 2.5)
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }',result)
     result=a1.currency_response('USD', 'y', 2.5)
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Exchange currency code is invalid." }',result)
     result=a1.currency_response('qwerty','asdfgh', 2)
     cornell.assert_equals('{ "success" : false, "lhs" : "", "rhs" : "", "error" : "Source currency code is invalid." }',result)
    
def testD():
     """Test procedure for Part A"""
     result=a1.iscurrency('USD')
     cornell.assert_true(True)
     result=a1.iscurrency('')
     cornell.assert_equals(False,result)
     result=a1.iscurrency('E')
     cornell.assert_equals(False,result)
     result=a1.iscurrency('zxcvbn')
     cornell.assert_equals(False,result)
     
     result=a1.exchange('USD','EUR',2.5)
     cornell.assert_floats_equal(2.0952375,result)
     result=a1.exchange('SVC','GEL',3.5254023347401)
     cornell.assert_floats_equal(1,result)
     result=a1.exchange('USD','EUR',3)
     cornell.assert_floats_equal(2.514285,result)
    
testA()
testB()
testC()
testD()
print("Module a1 passed all tests")
    
