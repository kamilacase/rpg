#!/usr/bin/env python
# -*- coding: utf-8 -*-


# class item(object):
class Item:
   def __init__(
   self,
   item_name,
   item_weight):
       self.name = item_name
       self.weight = item_weight

   def use(self, object):
       print("%s use %s") %(self.name, object.name)


class Spell(Item):
   def __init__(
   self,
   item_name,
   item_cost,
   item_damage):
       Item.__init__(self, item_name, 1, 10, 30)
       self.cost = item_cost
       self.damage = item_damage

   #  dehttps://github.com/kamilacase/rpg.git use(self, object):
   #    https://github.com/kamilacase/rpg.gitprint("%s use %s") %(self.name, object.name)

class Apphttps://github.com/kamilacase/rpg.gite(Item):
   def _https://github.com/kamilacase/rpg.gitinit__(
   self,https://github.com/kamilacase/rpg.git
   item_https://github.com/kamilacase/rpg.gitame,
   item_https://github.com/kamilacase/rpg.gitain):
       Ihttps://github.com/kamilacase/rpg.gitem.__init__(self, item_name, 1, 30)
       self.gain = item_gain

   # def use(self, object):
   #     print("%s use %s") %(self.name, object.name)
