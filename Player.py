""" Creates a player object that is used to identify the
    user's player created and the properties the user has
    acquired. The object must have a name, stats, inventory
    experience, and a level as properties."""
class Player(object):
    #Initializes Player object
    def __init__(self):
        object.__init__(self)
        #Creates a player name property
        self.playerName = "Nohbody"
        #Creates a property for player stats
        self.playerStats = {"health": 20,
                            "accuracy": 1,
                            "strength": 1,
                            "defense": 1,
                            "archery": 1,
                            "magic": 1}
        #Creates a property for player Inventory
        self.playerInventory = {"gold": 300}
        #Creates a property for player experience
        self.playerExperience = 0
        #Creates a property for the level of the player
        self.playerLevel = 0

    #Creates a method to retrieve player name
    def getplayerName(self):
        return self.playerName

    #Creates a method to change player name
    def setplayerName(self, name = "Nohbody"):
        self.playerName = name

    #Creates a method to retrieve player stats
    def getplayerStats(self):
        return self.playerStats

    #Creates a method to change player stats
    def setplayerStats(self,
                        health = 20,
                        accuracy = 1,
                        strength = 1,
                        defense = 1,
                        archery = 1,
                        magic = 1):
        self.playerStats["health"] = health
        self.playerStats["accuracy"] = accuracy
        self.playerStats["strength"] = strength
        self.playerStats["defense"] = defense
        self.playerStats["archery"] = archery
        self.playerStats["magic"] = magic

    #Creates a method to retrieve player experience
    def getplayerExperience(self):
        return self.playerExperience

    #Creates a method to alter player experience
    def setplayerExperience(self, experience):
        self.playerExperience = experience

    #Creates a method to retrieve player level
    def getplayerLevel(self):
        return self.playerLevel

    #Creates a method to level up a player
    def levelUp(self):
        keepGoing = True
        #Creates a loop that will increase a player's level by evaluating the
        #player's experience and determining whether the limit has been breached
        #or not. If the limit has been exceeded the player's level will increase
        #by one.
        while keepGoing:
            limit = 80 + (5 * self.getplayerLevel() ** 2)
            if self.getplayerExperience() >= limit:
                self.playerLevel += 1
                experience = self.getplayerExperience() - limit
                self.setplayerExperience(experience)
            else:
                keepGoing = False

#Debugging main function
def main():
    h = Player()
    h.setplayerExperience(300)
    h.levelUp()
    print h.getplayerLevel()

if __name__ == "__main__":
    main()
