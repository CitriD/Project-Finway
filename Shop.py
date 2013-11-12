from Player import *
from Item import *
from Sword import *
from Staff import *
from Bow import *
player = Player()
#Creates a Shop object which will function as the shop
#for the game. The shop will allow the player to purchase
#items or upgrade items all ready purchased.
class Shop(object):
    def __init__(self):
        Sword1 = Sword(1)
        Sword2 = Sword(2)
        Sword3 = Sword(3)
        Staff1 = Staff(1)
        Staff2 = Staff(2)
        Staff3 = Staff(3)
        Bow1 = Bow(1)
        Bow2 = Bow(2)
        Bow3 = Bow(3)

        self.inventory = {Sword1.getitemName(): 100,
                          Staff1.getitemName(): 100,
                          Bow1.getitemName(): 100,
                          Sword2.getitemName(): 200,
                          Staff2.getitemName(): 200,
                          Bow2.getitemName(): 200,
                          Sword3.getitemName(): 300,
                          Staff3.getitemName(): 300,
                          Bow3.getitemName(): 300}

    def getInventory(self):
        return self.inventory

    def upgrade(self, player, item):
        tier = item.getitemTier()
        cost = int(100 * (tier ** 1.2))
        player.playerInventory["gold"] -= cost
        item.setitemTier(1)
        item.tierAdjustment()

    def purchase(self, player, item):
        cost = self.inventory[item.getitemName()]
        player.playerInventory["gold"] -= cost
        player.playerInventory[item] = item.getitemName()

def main():
    sword = Sword(1)
    s = Shop()
    Eugene = Player()
    print Eugene.playerInventory
    s.purchase(Eugene, sword)
    print Eugene.playerInventory
    print Eugene.playerInventory[sword]
    s.upgrade(Eugene, sword)
    print Eugene.playerInventory




main()