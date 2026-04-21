#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:38:13 2026

@author: oliver
"""

def f(x):
    y = float(x**3 + 8)
    
    return y

def main(x):
    
    print(f(x))
    if f(x)>27:
        print("YAY!")
        
if __name__ == "__main__":
    main(float(input("X VAL")))