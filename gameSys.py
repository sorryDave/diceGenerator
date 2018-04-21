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
    def __init__(self, name="", age=0, hp=0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.name=name
        self.age=age
        self.hp = hp
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma = charisma
        
        #damage/inventory(class?)/armour/weapons(class weapon?)
        
    def damage():
        pass
         
    def initialRoll(D6):
        # tirada de 4D6, meter en array, ordenar de mayor a menor y y elegir los tres primeros
        pass
    
    def setModificators():
        #(hability - 10) / 2
        pass
    
    
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age=age
    def setHp(self, hp):
        self.hp = hp
    def setStrength(self, strength):
        self.strength = strength
    def setDexterity(self, dexterity):
        self.dexterity = dexterity
    def setConstitution(self, constitution):
        self.constitution = constitution
    def setIntelligence(self, intelligence):
        self.intelligence=intelligence
    def setWisdom(self, wisdom):
        self.wisdom=wisdom
    def setCharisma(self, charisma):
        self.charisma=charisma
        
    def printStats(self):
        print("printing...stats")
        print("\nname: {}\nhealth: {}\nage: {}\nstrength: {}\ndexterity: {}\nconstitution: {}\nintelligence: {}\nwisdom: {}\ncharisma: {}".format(self.name, self.hp, self.age, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma))
    

class Dice:
    #D6,D20
    #def dice roll():
    pass
    
class DiceRoll:
    pass


class Inventory:
    pass

class Armour:
    pass

class weapon:
    pass

class Monster:
    def __init__(self, name="", age=0, hp=0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.name=name
        self.age=age
        self.hp = hp
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma = charisma
        
        #self.dp = damage()
        
    def damage():
        pass
         
    def initialRoll():
        # cada monstruo tiene stats diferentes según el manual
        pass
    
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age=age
    def setHp(self, hp):
        self.hp = hp
    def setStrength(self, strength):
        self.strength = strength
    def setDexterity(self, dexterity):
        self.dexterity = dexterity
    def setConstitution(self, constitution):
        self.constitution = constitution
    def setIntelligence(self, intelligence):
        self.intelligence=intelligence
    def setWisdom(self, wisdom):
        self.wisdom=wisdom
    def setCharisma(self, charisma):
        self.charisma=charisma
        
    def printStats(self):
        print("printing...stats")
        print("\nname: {}\nhealth: {}\nage: {}\nstrength: {}\ndexterity: {}\nconstitution: {}\nintelligence: {}\nwisdom: {}\ncharisma: {}".format(self.name, self.hp, self.age, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma))
    
  

class Combat:
    # tirada de D20 / comparar con armadura de monstruo / superado: tirada de daño / no superado: fallo
    #Criticos y pifias 20 / 1
    
    # avanzado: posiciones de ventaja: diagonal/detras
    pass
  
human1 = Human("gawain", 29, 100, 9)

human1.printStats()






#modificadores de habilidades regla: (habilidad - 10)/2
#    strength / dexterity / Constitution / inteligence /wisdom / Charisma 
#       tirada para habilidades sD4 y escoger los tres mas altos
    