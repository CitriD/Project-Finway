from Item import *
from Player import *

#Creates a Sword object so that each tier will be able to inherit
#the properties of the sword. The Sword object will have its parent object
#being an Item.
class Sword(Item):
    #Initializes Bow object with a defualt tier set to 0
    def __init__(self, tier = 0):
        Item.__init__(self, Type = "sword")
        #Allows the item tier to be set in initialization of instance
        self.itemTier = tier
        #Creates a property for stats of Sword
        self.setitemStats(health = 0,
                                     accuracy = 5,
                                     strength = 10,
                                     defense = 5,
                                     archery = 0,
                                     magic = 0)
        #Calls tierAdjustment method to rename Bow and modify base stats
        self.tierAdjustment()


