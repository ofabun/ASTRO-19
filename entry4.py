#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:49:11 2026

@author: oliver
"""

class fav_animal:
    def __init__(self, name, arm_length, leg_length, number_of_eyes, tail, fur):
        self.name = name
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.number_of_eyes = number_of_eyes
        self.tail = tail
        self.fur = fur
        
    def describe_animal(self):
        print(f"Here are some details about {self.name}s.")
        print(f"{self.name}s have arms that are, on average, {self.arm_length} long.")
        print(f"{self.name}s have legs that are, on average, {self.leg_length} long.")
        print(f"{self.name}s typically have {self.number_of_eyes} eyes.")
        if self.tail:
            print(f"{self.name}s have tails.")
        else:
            print(f"{self.name}s have no tail.")
        if self.fur:
            print(f"{self.name}s are furry.")
        else:
            print(f"{self.name}s are not furry.")
            
my_favorite_animal = fav_animal(
    name="Cat",
    arm_length="10 cm",
    leg_length="22 cm", 
    number_of_eyes=2, 
    tail=True, 
    fur=True
)

my_favorite_animal.describe_animal()
