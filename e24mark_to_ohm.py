"""

1211am 11/21/22 Start
E24 surface mount resistor reader feature
1236am Finished


"""


def chip_resistor_e24_code(marking):
    digits = marking[0] + marking[1]
   
    multiplier = ""
    for zeros in range(int(marking[2])):
        multiplier += str(zeros)

    return digits + multiplier

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
