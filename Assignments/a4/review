#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 00:09:33 2018

@author: frank
"""

class A(object):
    x=3
    y=5
    
    def __init__(self,y):
        self.y=y
        
    def f(self):
        return self.g()
    
    def g(self):
        return self.x+self.y

class B(A):
    y=4
    z=10
    def __init__(self,x,y):
         self.x=x
         self.y=y
         
    def g(self):
        return self.x+self.z
        
    def h(self):
        return 42
        