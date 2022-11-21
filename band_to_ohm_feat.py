"""
Resistor reader algorithm 
Feature that calculates amount of Ohms based on number of bands and their color schemes 
"""

# get digit values
def digit(reply):

    match reply.lower():       
        case "black" | "bl":
            return "0"
        case "brown" | "br":
            return "1"
        case "red" | "r":
            return "2"
        case "orange" | "o":
            return "3"
        case "yellow" | "y":
            return "4"
        case "green" | "gr":
            return "5"
        case "blue" | "b":
            return "6"
        case "purple" | "v":
            return "7"
        case "gray" | "gy":
            return "8"
        case "white" | "w":
            return "9"
        case _:
            print("wrong color")
            return None

# get multiplier values 
def multiplier(reply):
    
    match reply.lower():
        case "black" | "bl":
            return 1
        case "brown" | "br":
            return 10
        case "red" | "r":
            return 100
        case "orange" | "o":
            return 1000
        case "yellow" | "y":
            return 10000
        case "green" | "gr":
            return 100000
        case "blue" | "b":
            return 1000000
        case "purple" | "v":
            return 10000000
        case "gray" | "gy":
            return 100000000
        case "white" | "w":
            return 1000000000
        case "gold" | "g":
            return 0.1
        case "silver" | "si":
            return 0.01  
        case _:
            print("wrong color")
            return None

# get tolerance values in percentages
def tolerance(reply):
    
    match reply.lower():
        case "brown" | "br":
            return 1
        case "red" | "r":
            return 2
        case "green" | "gr":
            return 0.5
        case "blue" | "b":
            return 0.25
        case "purple" | "v":
            return 0.1
        case "gray" | "gy":
            return 0.05
        case "gold" | "g":
            return 5
        case "silver" | "si":
            return 10  
        case _:
            print("wrong color")
            return None

#calculates the resistance value of the 3 band resistor
def three_band():

    digits = ""
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
    resistance = int(digits) * zeros
 
    return f"Resistance value is {resistance} ohms"

#calculates the resistance value range of the 4 band resistor
def four_band():

    digits = ""
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
    resistance = int(digits) * zeros
    string = f"Resistance value is {resistance} ohms\n"

    tolerance_value = resistance * (variety / 100)
    string += f"Tolerance value [ +/-{variety}% ] is {tolerance_value} ohms\n"
    
    ohms_safe = resistance + tolerance_value  #upper limit
    ohms_unsafe = resistance - tolerance_value  #lower limit
    
    string += f"The range is from {ohms_unsafe} ohms to {ohms_safe} ohms\n"
    string += f"Recommended number of ohms is {resistance} ohms to {ohms_safe}"

    return string

#calculates the resistance value range of the 5 band resistor
def five_band():

    digits = ""
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
    resistance = int(digits) * zeros
    string = f"Resistance value is {resistance} ohms\n"

    tolerance_value = resistance * (variety / 100)
    string += f"Tolerance value [ +/-{variety}% ] is {tolerance_value} ohms\n"
    
    ohms_safe = resistance + tolerance_value  #upper limit
    ohms_unsafe = resistance - tolerance_value  #lower limit
    
    string += f"The range is from {ohms_unsafe} ohms to {ohms_safe} ohms\n"
    string += f"Recommended number of ohms is {resistance} ohms to {ohms_safe}"

    return string

# main function
def main():
    
    while True:
        bands = int(input("How many bands? "))

        match bands:
            case 3:
                result = three_band()
                if result == None:
                    print("Invalid color scheme for 3 band resistor.")
                else:
                    print(result)
                    break
            case 4:
                result = four_band()
                if result == None:
                    print("Invalid color scheme for 4 band resistor.")
                else:
                    print(result)
                    break
            case 5:
                result = five_band()
                if result == None:
                    print("Invalid color scheme for 5 band resistor.")
                else:
                    print(result)
                    break
            case _: 
                print("3-5 bands only")
   
if __name__ == "__main__":
    main()
