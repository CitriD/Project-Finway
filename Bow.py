from Item import *
from Player import *

#Creates a Bow object so that each tier will be able to inherit
#the properties of the bow. The Bow object will have its parent object
#being an Item.
class Bow(Item):
    #Initializes Bow object with a defualt tier set to 0
    def __init__(self, tier = 0):
        Item.__init__(self, Type = "bow")
        #Allows the item tier to be set in initialization of instance
        self.itemTier = tier
        #Creates a property for stats of Bow
        self.setitemStats(health = 0,
                                     accuracy = 5,
                                     strength = 0,
                                     defense = 5,
                                     archery = 10,
                                     magic = 0)
        #Calls tierAdjustment method to rename Bow and modify base stats
        self.tierAdjustment()

