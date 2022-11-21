"""
This module's algorithm will decipher chip resistor markings in E96
Separate feature to RRV2
Started since 7:11pm 11/19/2022 Saturday
Completed 11/19/2022 952pm.

1001pm
The algorithm can make you input the resistor marking again if the marking is not
exactly 3 characters.
But if either the digits or the letter is not valid, the _ case will trigger and the
algorithm will not calculate the resistance. I want the algorithm to make the user
input the whole marking sequence again until the sequence is just right.

1045pm
Updated the decision tree.

Was:

While Loop
    Read marking
    If marking length is 3:
        Start function
        Print result given by function
        Break Loop
    Else:
        Sequence is wrong. Try again

Now:

While Loop:
    Read marking
    if marking length < 3:
        print("Sequence is too short")
    elif marking length > 3:
        print(f"Sequence is too long")
    else
        if any character in marking is not valid by function:
            print("Invalid sequence. Try again")
        else:
            Print result given by function
            Break Loop

Now the While loop will not break until the proper sequence is inputted.

1240am 11/20/2022 Fully operational.

"""


def chip_resistor_e96_code(mark1):

    match mark1[0] + mark1[1]:  #get 3 digit from two characters of marking
        case "01":
            OHMS = 100
        case "02":
            OHMS = 102
        case "03":
            OHMS = 105
        case "04":
            OHMS = 107
        case "05":
            OHMS = 110
        case "06":
            OHMS = 113
        case "07":
            OHMS = 115
        case "08":
            OHMS = 118
        case "09":
            OHMS = 121
        case "10":
            OHMS = 124
        case "11":
            OHMS = 127
        case "12":
            OHMS = 130
        case "13":
            OHMS = 133
        case "14":
            OHMS = 137
        case "15":
            OHMS = 140
        case "16":
            OHMS = 143           
        case "17":
            OHMS = 147
        case "18":
            OHMS = 150
        case "19":
            OHMS = 154
        case "20":
            OHMS = 158
        case "21":
            OHMS = 162
        case "22":
            OHMS = 165
        case "23":
            OHMS = 169
        case "24":
            OHMS = 174
        case "25":
            OHMS = 178
        case "26":
            OHMS = 182
        case "27":
            OHMS = 187
        case "28":
            OHMS = 191
        case "29":
            OHMS = 196
        case "30":
            OHMS = 200
        case "31":
            OHMS = 205
        case "32":
            OHMS = 210     
        case "33":
            OHMS = 215
        case "34":
            OHMS = 221
        case "35":
            OHMS = 226
        case "36":
            OHMS = 232
        case "37":
            OHMS = 237
        case "38":
            OHMS = 243
        case "39":
            OHMS = 249
        case "40":
            OHMS = 255
        case "41":
            OHMS = 261
        case "42":
            OHMS = 267
        case "43":
            OHMS = 274
        case "44":
            OHMS = 280
        case "45":
            OHMS = 287
        case "46":
            OHMS = 294
        case "47":
            OHMS = 301
        case "48":
            OHMS = 309           
        case "49":
            OHMS = 316
        case "50":
            OHMS = 324
        case "51":
            OHMS = 332
        case "52":
            OHMS = 340
        case "53":
            OHMS = 348
        case "54":
            OHMS = 357
        case "55":
            OHMS = 365
        case "56":
            OHMS = 374
        case "57":
            OHMS = 383
        case "58":
            OHMS = 392
        case "59":
            OHMS = 402
        case "60":
            OHMS = 412
        case "61":
            OHMS = 422
        case "62":
            OHMS = 432
        case "63":
            OHMS = 442
        case "64":
            OHMS = 453        
        case "65":
            OHMS = 464
        case "66":
            OHMS = 475
        case "67":
            OHMS = 487
        case "68":
            OHMS = 499
        case "69":
            OHMS = 511
        case "70":
            OHMS = 523
        case "71":
            OHMS = 536
        case "72":
            OHMS = 549
        case "73":
            OHMS = 562
        case "74":
            OHMS = 576
        case "75":
            OHMS = 590
        case "76":
            OHMS = 604
        case "77":
            OHMS = 619
        case "78":
            OHMS = 634
        case "79":
            OHMS = 649
        case "80":
            OHMS = 665  
        case "81":
            OHMS = 600
        case "82":
            OHMS = 600
        case "83":
            OHMS = 710
        case "84":
            OHMS = 732
        case "85":
            OHMS = 750
        case "86":
            OHMS = 768
        case "87":
            OHMS = 787
        case "88":
            OHMS = 806
        case "89":
            OHMS = 825
        case "90":
            OHMS = 845
        case "91":
            OHMS = 866
        case "92":
            OHMS = 887
        case "93":
            OHMS = 909
        case "94":
            OHMS = 931
        case "95":
            OHMS = 953
        case "96":
            OHMS = 976
        case _:
            print(f"Invalid digit sequence: {mark1[0] + mark1[1]}")
            return None

    match mark1[2].upper():  #get multiplier from final character of marking
        case "A":
            MULTIPLIER = 1
        case "B" | "H":
            MULTIPLIER = 10
        case "C":
            MULTIPLIER = 100
        case "D":
            MULTIPLIER = 1000
        case "E":
            MULTIPLIER = 10000
        case "F":
            MULTIPLIER = 100000
        case "X" | "S":
            MULTIPLIER = 0.1
        case "R" | "Y":
            MULTIPLIER = 0.01
        case "Z":
            MULTIPLIER = 0.001
        case _:
            print(f"Invalid character: {mark1[2]}")
            return None

    resistance = OHMS * MULTIPLIER # get resistance
    tolerance = resistance * 0.01 # 1% tolerance
    
    ohm_high = resistance + tolerance # upper limit
    ohm_low = resistance - tolerance # lower limit
    
    return f"Resistance is {resistance} Ohms\nThe range is {ohm_low} to {ohm_high} Ohms"
    
def main():

    while True:
        marking = input("Resistor mark is: ")

        if len(marking) < 3:
            print("Sequence is too short")
        elif len(marking) > 3:
            print(f"Sequence is too long: {len(marking)} characters")
        else:
            if chip_resistor_e96_code(marking) == None:
                print("Invalid sequence. Try again")
            else:
                print(chip_resistor_e96_code(marking))
                break
        
if __name__ == "__main__":
    main()
