#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:41:24 2018

@author: hellodave


"""
import random

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
    def __init__(self, name="", age=0, hp=0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0, armour=0):
        self.name=name
        self.age=age
        self.hp = hp
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma = charisma
        self.armour = armour
        
        #damage/inventory(class?)/armour/weapons(class weapon?)
#        self.dice = DiceGenerator(6)
        
    def initialRoll(self):
        
        #    strength / dexterity / Constitution / inteligence /wisdom / Charisma 
        #
        pass
    
    def setModificators():
        #modificadores de habilidades regla: (habilidad - 10)/2
        #(hability - 10) / 2
        pass      
        
    def damage():
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
        print("\nname: {}\nhealth: {}\nage: {}\nstrength: {}\ndexterity: {}\nconstitution: {}\nintelligence: {}\nwisdom: {}\ncharisma: {}\narmour:{}".format(self.name, self.hp, self.age, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.armour))
    

#class DiceGenerator:
#    def __init__(self, sides):
#        self.sides=sides
#    def printSides(self):
#        print("D{}".format(self.sides))
#    
#    def roll(self, n=1):
#        print("Rolling dices...")
#        print("The values are....")
#        print(random.randint(n, self.sides))
#        print(random.randint(n,self.sides))
#    
#class DiceRoll:
#    pass


class Inventory:
    pass

class Armour:
    pass

class weapon:
    pass

class Monster:
    def __init__(self, name="", age=0, hp=0, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0, armour=0):
        self.name=name
        self.age=age
        self.hp = hp
        self.strength=strength
        self.dexterity=dexterity
        self.constitution=constitution
        self.intelligence=intelligence
        self.wisdom=wisdom
        self.charisma = charisma
        self.armour=armour
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
        print("\nname: {}\nhealth: {}\nage: {}\nstrength: {}\ndexterity: {}\nconstitution: {}\nintelligence: {}\nwisdom: {}\ncharisma: {}\narmour:{}".format(self.name, self.hp, self.age, self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.armour))
    
    
def diceroll(sides):
    n=1
    if sides == 6:
        print("\nrolling D6 dices...")
        print("The values are....")
        roll = random.randint(n,sides)
        print(roll)
    if sides == 20:
        print("\nrolling D20 dices...")
        print("The values are....")
        roll = random.randint(n,sides)
        print(roll)
    if sides ==4:
        print("\nrolling D4 dices...")
        print("The values are....")
        roll = random.randint(n,sides)
        print(roll)   
    return roll
 


def attack(p1,p2):
    if p2.hp > 0:
        dice_roll = diceroll(6) + diceroll(6)
        print("\n{} attack points: ".format(p1.name))
        print(dice_roll)
        return dice_roll
    else:
        print("{} is stunned or dead".format(p2))

       
def combat(p1, p2):
    if p1.armour < diceroll(20):
         res = attack(p1, p2)
         p2.hp -= res
         print("\n\t{} health is {}\n\n".format(p2.name, p2.hp))
         return res
    else:
         print("null attack")
         return 0;
         
    

def rounds(p1,p2):
    while monster1.hp > 0:
        combat(p1, p2)

#class Combat:
#    def __init__(self, pc, npc):
#        self.pcArmour = pc.armour
#        self.npcArmour = npc.armour
#        self.dice_roll = diceroll(20)
#        
#        def fight(self):
#            if self.npcArmour < self.dice_roll:
#                return True
#            else:
#                return False
#        
                
                
                
        
    # tirada de D20 / comparar con armadura de monstruo / superado: tirada de daño / no superado: fallo
    #Criticos y pifias 20 / 1
    
    # avanzado: posiciones de ventaja: diagonal/detras
    
  
human1 = Human("gawain", 20, 70, 70, armour = 7)

human1.printStats()

monster1 = Monster("kobold", 30, 70, 70, armour = 7)
monster1.printStats()
print("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")  

rounds(human1, monster1)



    