"""
Resistor reader algorithm 
Feature that calculates amount of Ohms based on number of bands and their color schemes 
Published 250am Nov 13, 2022 Sunday

"""

#dictionary 1
digits = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "purple": 7,
    "gray": 8,
    "white": 9,
}

#dictionary 2
places = {
    "black": 1,
    "brown": 10,
    "red": 100,
    "orange": 1000,
    "yellow": 10000,
    "green": 100000,
    "blue": 1000000,
    "purple": 10000000,
    "gray": 100000000,
    "white": 1000000000,
    "gold": 0.1,
    "silver": 0.01,
}

#dictionary 3
percent = {
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 0.5,
    "blue": 0.25,
    "purple": 0.1,
    "gray": 0.05,
    "gold": 5,
    "silver": 10,
}

"""
This function retrieves an integer value from dictionary 1
using string key
"""

def get_digit(reply):
    if reply == "black" or reply == "bl":
        return digits["black"]
    elif reply == "brown" or reply == "br":
        return digits["brown"]
    elif reply == "red" or reply == "r":
        return digits["red"]
    elif reply == "orange" or reply == "o":
        return digits["orange"]
    elif reply == "yellow" or reply == "y":
        return digits["yellow"]
    elif reply == "green" or reply == "gr":
        return digits["green"]
    elif reply == "blue" or reply == "b":
        return digits["blue"]
    elif reply == "purple" or reply == "v":
        return digits["purple"]
    elif reply == "gray" or reply == "gy":
        return digits["gray"]
    elif reply == "white" or reply == "w":
        return digits["white"]
    else:
        print("wrong color")
        
"""
This function retrieves a number value from dictionary 2
using string key
"""

def multiplier(reply):
    if reply == "black" or reply == "bl":
        return places["black"]
    elif reply == "brown" or reply == "br":
        return places["brown"]
    elif reply == "red" or reply == "r":
        return places["red"]
    elif reply == "orange" or reply == "o":
        return places["orange"]
    elif reply == "yellow" or reply == "y":
        return places["yellow"]
    elif reply == "green" or reply == "gr":
        return places["green"]
    elif reply == "blue" or reply == "b":
        return places["blue"]
    elif reply == "purple" or reply == "v":
        return places["purple"]
    elif reply == "gray" or reply == "gy":
        return places["gray"]
    elif reply == "white" or reply == "w":
        return places["white"]
    elif reply == "gold" or reply == "g":
        return places["gold"]
    elif reply == "silver" or reply == "si":
        return places["silver"]
    else:
        print("wrong color")
        
"""
This function retrieves a number value from dictionary 3
using string key
"""

def tolerance(reply):
    if reply == "brown" or reply == "br":
        return places["brown"]
    elif reply == "red" or reply == "r":
        return places["red"]
    elif reply == "orange" or reply == "o":
        return places["orange"]
    elif reply == "yellow" or reply == "y":
        return places["yellow"]
    elif reply == "green" or reply == "gr":
        return places["green"]
    elif reply == "blue" or reply == "b":
        return places["blue"]
    elif reply == "purple" or reply == "v":
        return places["purple"]
    elif reply == "gray" or reply == "gy":
        return places["gray"]
    elif reply == "gold" or reply == "g":
        return places["gold"]
    elif reply == "silver" or reply == "si":
        return places["silver"]
    else:
        print("wrong color")

#calculates the resistance value of the 3 band resistor
def three_band():
    b1 = get_digit(input("Color of 1st band? ").lower())
    b2 = get_digit(input("Color of 2nd band? ").lower())
    zeros = multiplier(input("Color of 3rd band? ").lower())
    
    ohm = int(str(b1) + str(b2)) * zeros
    
    print(f"{ohm} ohms")

#calculates the resistance value range of the 4 band resistor
def four_band():
    b1 = get_digit(input("Color of 1st band? ").lower())
    b2 = get_digit(input("Color of 2nd band? ").lower())
    zeros = multiplier(input("Color of 3rd band? ").lower())
    level = tolerance(input("Color of 4th band? ").lower())
    
    #resistance before tolerance
    ohm = int(str(b1) + str(b2)) * zeros
    print(f"Actual resistance value: {ohm} ohms")
    
    #actual tolerance
    smallohm = ohm * (level / 100)
    print(f"Tolerance value: {ohm} ohms")
    
    highohm = ohm + smallohm  #upper limit
    lowohm = ohm - smallohm    #lower limit
    
    print(f"{lowohm} ohms to {highohm} ohms")

#calculates the resistance value range of the 5 band resistor
def five_band():
    b1 = get_digit(input("Color of 1st band? ").lower())
    b2 = get_digit(input("Color of 2nd band? ").lower())
    b3 = get_digit(input("Color of 3rd band? ").lower())
    zeros = multiplier(input("Color of 4th band? ").lower())
    level = tolerance(input("Color of 5th band? ").lower())
    
    #resistance before tolerance
    ohm = int(str(b1) + str(b2) + str(b3))  * zeros
    print(f"Actual resistance value: {ohm} ohms")
    
    #actual tolerance
    smallohm = ohm * (level / 100)
    print(f"Tolerance value: {ohm} ohms")
    
    highohm = ohm + smallohm  #upper limit
    lowohm = ohm - smallohm    #lower limit
    
    print(f"{lowohm} ohms to {highohm} ohms")

#driver
while True:
    bands = int(input("How many bands? "))
    if bands == 3:
        three_band()
        break
    elif bands == 4:
        four_band()
        break
    elif bands == 5:
        five_band()
        break
    elif bands < 3:
        print("Your number is too small")
    elif bands > 5:
        print("Your number is too large")
        
