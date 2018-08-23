#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Character(object):
class Character:
    def __init__(
    self,
    character_name,
    character_health,
    character_mana,
    character_exp ,
    character_power):
        self.name = character_name
        self.health = character_health
        self.mana = character_mana
        self.exp = character_exp
        self.power = character_power

    def description(self):
        print("%s: health:%s, mana:%s, exp:%s, power:%s, inventory:%s") %(self.name, self.health, self.mana, self.exp, self.power, self.inventory)

    def move(self, x, y):
        print("%s move") %(self.name)

    def attack(self, opponent):
        print("%s attack %s") %(self.name, opponent.name)

    def throw(self, object):
        print("%s drop %s") %(self.name, object.name)

    def use(self, object):
        print("%s use %s") %(self.name, object.name)

class Wizard(Character):
    def __init__(
    self,
    character_name = 'unknow',
    character_health = 0,
    character_mana = 0,
    character_exp = 0,
    character_power = 0,
    character_inventory = [],
    character_spell = []):
        self.spell = character_spell

    def use(self, object):
        print("%s use %s") %(self.name, object.name)

class Warrior(Character):
    def __init__(
    self,
    character_name = 'unknow',
    character_health = 0,
    character_mana = 0,
    character_exp = 0,
    character_power = 0,
    character_inventory = [],
    character_spell = []):
        self.spell = character_spell

    def use(self, object):
        print("%s use %s") %(self.name, object.name)




Malone = Character("Malone", 10, 50, 0, 10)
Malone.description()
Wizard = Character("plop", 10, 60, 0, 0)
Wizard.description()
Warrior = Character("Yup",10,40, 0,20)
Warrior.description()



