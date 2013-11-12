""" Creates an Item object that will have instances that functions as
    items throughout the game. The Item object will be used for player
    inventory and the shop object. Items need properties for type, name,
    tier, and stats. An item's name needs to be able to be adjusted based
    on its name and type."""
class Item(object):
    #Initializes Item object with a type and tier
    def __init__(self, Type = "none", tier = 1):
        object.__init__(self)
        #Creates an item Type property
        self.itemType = Type
        #Creates an Item Name property that is defined by type and tier of item
        self.itemName = ("Tier %i %s" %(tier, Type))
        #Creates an Item tier property
        self.itemTier = tier
        #Creates an item's stats property
        self.itemStats = {"health": 0,
                          "accuracy": 0,
                          "strength": 0,
                          "defense": 0,
                          "archery": 0,
                          "magic": 0,}

    #Creates a method used to retrieve item's type
    def getitemType(self):
        return self.itemType

    #Creates a method used to set an item's type
    def setitemType(self, Type):
        self.itemType = Type

    #Creates a method used to retrieve Item's name
    def getitemName(self):
        return self.itemName

    #Creates a method used to assign an Item's name
    def setitemName(self, Type, tier):
        self.itemName = ("Tier %i %s" %(tier, Type))

    #Creates a method to retrieve item's tier value
    def getitemTier(self):
        return self.itemTier

    #Creates a method to set an itemTier value
    def setitemTier(self, tier):
        self.itemTier += tier

    #Creates a method to retrieve stats of an item
    def getitemStats(self):
        return self.itemStats

    #Creates a method to set the stats of an item
    def setitemStats(self,
                     health = 0,
                     accuracy = 0,
                     strength = 0,
                     defense = 0,
                     archery = 0,
                     magic = 0):
        self.itemStats["health"] = health
        self.itemStats["accuracy"] = accuracy
        self.itemStats["strength"] = strength
        self.itemStats["defense"] = defense
        self.itemStats["archery"] = archery
        self.itemStats["magic"] = magic

    #Creates a method to adjust the name of an item and its stats based on its
    #type and tier.
    def tierAdjustment(self):
        self.setitemName(self.getitemType(), self.getitemTier())
        self.setitemStats(health = int((self.itemStats["health"] * (self.getitemTier() ** .5))),
                          accuracy = int((self.itemStats["accuracy"] * (self.getitemTier() ** .5))),
                          strength = int((self.itemStats["strength"] * (self.getitemTier() ** .5))),
                          defense = int((self.itemStats["defense"] * (self.getitemTier() ** .5))),
                          archery = int((self.itemStats["archery"] * (self.getitemTier() ** .5))),
                          magic = int((self.itemStats["magic"] * (self.getitemTier() ** .5))))

#Debugging main function
def main():
    sword1 = Item("Sword", 1)
    sword1.setitemStats(health = 20, accuracy = 5, strength = 10, defense = 2)
    print sword1.getitemTier()
    print sword1.getitemName()
    print sword1.getitemStats()
    sword1.setitemTier(2)
    sword1.tierAdjustment()
    #sword2 = sword1.setitemTier(1)
    print sword1.getitemName()
    print sword1.getitemStats()

main()
