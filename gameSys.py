#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:41:24 2018

@author: hellodave
"""
#
#import datetime # we will use this for date objects
#
#class Person:
#
#    def __init__(self, name, surname, birthdate, address, telephone, email):
#        self.name = name
#        self.surname = surname
#        self.birthdate = birthdate
#
#        self.address = address
#        self.telephone = telephone
#        self.email = email
#
#    def age(self):
#        today = datetime.date.today()
#        age = today.year - self.birthdate.year
#
#        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#            age -= 1
#
#        return age
#
#person = Person(
#    "Jane",
#    "Doe",
#    datetime.date(1992, 3, 12), # year, month, day
#    "No. 12 Short Street, Greenville",
#    "555 456 0987",
#    "jane.doe@example.com"
#)
#
#print(person.name)
#print(person.email)
#print(person.age())
#


class Human:
    def __init__(self, name, age, health, strength):
        self.name=name
        self.age=age
        self.health = health
        self.strength=strength
        #self.dexterity=dexterity
        #self.intelligence=intelligence
        #self.wisdom=wisdom
        #self.damage = 0
    
    def printStats(self):
        print("printing...stats")
        print("\nname: {}\nhealth:{}\nage{}\nstrength:{}".format(self.name, self.health, self.age, self.strength))
    def setHealth(h):
        pass        
        
        
  
    
human1 = Human("gawain", 29, 100, 9)


class diceRoll:
    pass
    