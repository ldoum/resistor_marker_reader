"""

1211am 11/21/22
E24 surface mount resistor reader feature



"""


def chip_resistor_e24_code(marking):
    digits = mark1[0] + mark1[1]
    
    if digits <= 0 or digits > 99:
        return None

    multiplier = ""
    for zeros in range(mark1[2]):
        multiplier += zeros

    resistance = digits * int(multiplier)

    return resistance



def main():

    while True:
        marking = int(input("Resistor mark is: "))

        if len(marking) < 3:
            print("Sequence is too short")
        elif len(marking) > 3:
            print(f"Sequence is too long: {len(marking)} characters")
        else:
            if chip_resistor_e24_code(marking) == None:
                print("Invalid sequence. Try again")
            else:
                print(chip_resistor_e24_code(marking))
                break
        
if __name__ == "__main__":
    main()
