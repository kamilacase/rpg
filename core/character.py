#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class Character(object):
class Character:
    def __init__(
    self,
    character_name,
    character_health,
    character_mana,
    character_power,
    character_xp):
        self.name = character_name
        self.health = character_health
        self.mana = character_mana
        self.power = character_power
        self.xp = character_xp
        self.inventory = []

    def attack(self, enemy):
        self.xp += 10
        enemy.health = 0

    def pick(self, inventory[item]):
            self.inventory = inventory[item]




    # def description(self):
    #     print("%s: health:%s, mana:%s, power:%s, xp:%s, inventory:%s") %(self.name, self.health, self.mana, self.power, self.xp, self.inventory)
    #
    # def move(self, x, y):
    #     print("%s move") %(self.name)
    #
    # def attack(self, opponent):
    #     print("%s attack %s") %(self.name, opponent.name)
    #
    # def throw(self, object):
    #     print("%s throw %s") %(self.name, object.name)
    #
    # def use(self, object):
    #     print("%s use %s") %(self.name, object.name)




class Wizard(Character):
    def __init__(
    self,
    character_name):
        Character.__init__(self, character_name, 100, 100, 50, 0)
        self.spells =  []

    def use(self, object):
        print("%s use %s") %(self.name, object.name)

class Warrior(Character):
    def __init__(
    self,
    character_name,
    character_armor):
        Character.__init__(self, character_name, 200, 0, 300, 0)
        self.armor = character_armor

    def use(self, object):
        print("%s use %s") %(self.name, object.name)
