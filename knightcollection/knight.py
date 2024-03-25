class Knight:
    """
    This class represents a knight in a chess game    

    params:
    name: string
        name of the knight 
    strength: int
        strength of the knight
    agility: int
        agility of the knight
    specialArmor: string
        special armor of the knight
    """

    def __init__(self, name, strength, agility, specialArmor):
        self.name = str(name)
        self.strength = int(strength)
        self.agility = int(agility)
        self.specialArmor = str(specialArmor)

    #this is a magic method that is called when the object is printed
    def __str__(self):
        return "Name: " + self.name + "\nStrength: " + str(self.strength) + "\nAgility: " + str(self.agility) + "\nSpecial Armor: " + self.specialArmor
    #render the knightin good format
    """
    This method renders the knight in a good format.
    params:
    index: int (not required)
        the index of the knight in the list
    """
    def render(self,index=0):
        if index == 0:
            print("====================================")
            print("Name: " + self.name)
            print("Strength: " + str(self.strength))
            print("Agility: " + str(self.agility))
            print("Special Armor: " + self.specialArmor)
            print("====================================")
        else:
            print(f"number:{index}=====================")
            print("Name: " + self.name)
            print("Strength: " + str(self.strength))
            print("Agility: " + str(self.agility))
            print("Special Armor: " + self.specialArmor)
            print("====================================")