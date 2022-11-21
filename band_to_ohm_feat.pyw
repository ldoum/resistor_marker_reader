"""
Resistor reader algorithm 
Feature that calculates amount of Ohms based on number of bands and their color schemes 
"""
def digit(reply):
    match reply.lower():       
        case "black" | "bl":
            DIGITS = 0
        case "brown" | "br":
            DIGITS = 1
        case "red" | "r":
            DIGITS = 2
        case "orange" | "o":
            DIGITS = 3
        case "yellow" | "y":
            DIGITS = 4
        case "green" | "gr":
            DIGITS = 5
        case "blue" | "b":
            DIGITS = 6
        case "purple" | "v":
            DIGITS = 7
        case "gray" | "gy":
            DIGITS = 8
        case "white" | "w":
            DIGITS = 9
        case _:
            print("wrong color")
            return None

def multiplier(reply):
    match reply.lower():
        case "black" | "bl":
            MULTIPLIER = 1
        case "brown" | "br":
            MULTIPLIER = 10
        case "red" | "r":
            MULTIPLIER = 100
        case "orange" | "o":
            MULTIPLIER = 1000
        case "yellow" | "y":
            MULTIPLIER = 10000
        case "green" | "gr":
            MULTIPLIER = 100000
        case "blue" | "b":
            MULTIPLIER = 1000000
        case "purple" | "v":
            MULTIPLIER = 10000000
        case "gray" | "gy":
            MULTIPLIER = 100000000
        case "white" | "w":
            MULTIPLIER = 1000000000
        case "gold" | "g":
            MULTIPLIER = 0.1
        case "silver" | "si":
            MULTIPLIER = 0.01  
        case _:
            print("wrong color")
            return None

def tolerance(reply):
    match reply.lower():
        case "brown" | "br":
            TOLERANCE = 1
        case "red" | "r":
            TOLERANCE = 2
        case "green" | "gr":
            TOLERANCE = 0.5
        case "blue" | "b":
            TOLERANCE = 0.25
        case "purple" | "v":
            TOLERANCE = 0.1
        case "gray" | "gy":
            TOLERANCE = 0.05
        case "gold" | "g":
            TOLERANCE = 5
        case "silver" | "si":
            TOLERANCE = 10  
        case _:
            print("wrong color")
            return None

#calculates the resistance value of the 3 band resistor
def three_band():
    for count in range(2):
        number = digit(input(f"Color of band {count + 1}: ")) #get bands 1 and 2
        if number == None:
            return None
        else:
            digits += number
        
    zeros = multiplier(input("Color of band 3: "))
    if zeros == None:
        return None

    #write
    resistance = digits * zeros
 
    return f"Resistance value is {resistance} ohms"

#calculates the resistance value range of the 4 band resistor
def four_band():
    for count in range(2):
        number = digit(input(f"Color of band {count + 1}: ")) #get bands 1 and 2
        if number == None:
            return None
        else:
            digits += number
        
    zeros = multiplier(input("Color of band 3: "))
    if zeros == None:
        return None
    
    variety = tolerance(input("Color of band 4: "))
    if variety == None:
        return None

    #write
    resistance = digits * zeros
    string += f"Resistance value is {resistance} ohms\n"

    tolerance_value = resistance * (variety / 100)
    string += f"Tolerance value [ +/-{variety}% ] is {tolerance_value} ohms\n"
    
    ohms_safe = ohm + tolerance_value  #upper limit
    ohms_unsafe = ohm - tolerance_value  #lower limit
    
    string += f"The range is {ohms_unsafe} ohms - {ohms_safe} ohms\n"
    string += f"Recommended number of ohms is {resistance} ohms to {ohms_safe}"

    return string

#calculates the resistance value range of the 5 band resistor
def five_band():
    for count in range(3):
        number = digit(input(f"Color of band {count + 1}: ")) #get bands 1, 2, and 3
        if number == None:
            return None
        else:
            digits += number
        
    zeros = multiplier(input("Color of band 4: "))
    if zeros == None:
        return None
    
    variety = tolerance(input("Color of band 5: "))
    if variety == None:
        return None

    #write
    resistance = digits * zeros
    string += f"Resistance value is {resistance} ohms\n"

    tolerance_value = resistance * (variety / 100)
    string += f"Tolerance value [ +/-{variety}% ] is {tolerance_value} ohms\n"
    
    ohms_safe = ohm + tolerance_value  #upper limit
    ohms_unsafe = ohm - tolerance_value  #lower limit
    
    string += f"The range is {ohms_unsafe} ohms - {ohms_safe} ohms\n"
    string += f"Recommended number of ohms is {resistance} ohms to {ohms_safe}"

    return string

def main():
    
    while True:
        bands = int(input("How many bands? "))

        match bands:
            case 3:
                if three_band() == None:
                    print("Invalid color scheme for 3 band resistor.")
                else:
                    three_band()
                    break
            case 4:
                if four_band() == None:
                    print("Invalid color scheme for 4 band resistor.")
                else:
                    four_band()
                    break
            case 5:
                if five_band() == None:
                    print("Invalid color scheme for 5 band resistor.")
                else:
                    five_band()
                    break
            case _: 
                print("3-5 bands only")
   
if __name__ == "__main__":
    main()
