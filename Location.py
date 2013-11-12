from Player import *
Player = Player()

""" Creates a Location object that requires a name
    and its appropriate effects to stats."""
class Location(object):
    #Initializes Location object
    def __init__(self):
        object.__init__(self)
        #Creates a location name property
        self.locationName = ""
        #Cretaes a stat effects property
        self.statEffects = {"health": 1,
                            "accuracy": 1,
                            "strength": 1,
                            "defense": 1,
                            "archery": 1,
                            "magic": 1}

    #Creates a method to retrieve location name
    def getlocationName(self):
        return self.locationName

    #Creates a method to set location name
    def setlocationName(self, name):
        self.locationName = name

    #Creates a method to retrieve stat effects
    def getstatEffects(self):
        return self.statEffects

    #Creates a method to adjust stat effects.
    def setstatEffects(self,
                       health = 1,
                       accuracy = 1,
                       strength = 1,
                       defense = 1,
                       archery = 1,
                       magic = 1):
        self.statEffects["health"] = health
        self.statEffects["accuracy"] = accuracy
        self.statEffects["strength"] = strength
        self.statEffects["defense"] = defense
        self.statEffects["archery"] = archery
        self.statEffects["magic"] = magic

    #Creats a method to apply stat effects to a  player's stats
    def effectPlayer(self, player):
        #for i in self.statEffects:
            #player.setplayerStats(i = (player.playerStats[i] * self.statEffects[i]))
        player.setplayerStats(health = (player.playerStats["health"] * self.statEffects["health"]),
                              accuracy = (player.playerStats["accuracy"] * self.statEffects["accuracy"]),
                              strength = (player.playerStats["strength"] * self.statEffects["strength"]),
                              defense = (player.playerStats["defense"] * self.statEffects["defense"]),
                              archery = (player.playerStats["archery"] * self.statEffects["archery"]),
                              magic = (player.playerStats["magic"] * self.statEffects["magic"]))

#Debugging main function
def main():
    l = Location()
    l.setlocationName("The Pit")
    l.setstatEffects(strength = .7, archery = .5, health = .3)
    print l.getstatEffects()
    #print l.getlocationName()
    print Player.getplayerStats()
    l.effectPlayer(Player)
    print Player.getplayerStats()

main()


