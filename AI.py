""" The AI object will be used to create instances of
    Enemy AI opponents. The opponent will require a name,
    stats, and a level."""
class AI(object):
    #initializes AI object
    def __init__(self):
        object.__init__(self)
        #creates a name property with an empty string as its value
        self.AIname = ""
        #creates a dictionary of stats with a default value of 0
        self.AIstats = {"health": 0,
                        "accuracy": 0,
                        "strength": 0,
                        "defense": 0,
                        "archery": 0,
                        "magic": 0,}
        #creates a level property with a default valu of 0
        self.AIlevel = 0

    #creates a method to get the name of the AI
    def getAIname(self):
        return self.AIname

    #creates a method to set the name of the AI
    def setAIname(self, name):
        self.AIname = name

    #creates a method that retrieves the stats of the AI
    def getAIstats(self):
        return self.AIstats

    #creates a method that sets the stats of the AI
    def setAIstats(self,
                       health = 0,
                       accuracy = 0,
                       strength = 0,
                       defense = 0,
                       archery = 0,
                       magic = 0):
        self.AIstats["health"] = health
        self.AIstats["accuracy"] = accuracy
        self.AIstats["strength"] = strength
        self.AIstats["defense"] = defense
        self.AIstats["archery"] = archery
        self.AIstats["magic"] = magic

    #creates a method that gets the level of the AI
    def getAIlevel(self):
        return self.AIlevel

    #creates a method that sets the level of the AI
    def setAIlevel(self, level):
        self.AIlevel = level

#Debugging main function
def main():
    Boss = AI()
    Boss.setAIname("Gregory")
    Boss.setAIstats(health = 50, accuracy = 20, strength = 32, defense = 99, magic = 2)
    Boss.setAIlevel(5)
    print Boss.AIname
    print Boss.getAIstats()
    print Boss.getAIlevel()

main()
