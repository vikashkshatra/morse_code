

from typing import Dict


codes={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/"
        }


a = input("Enter your phrase: \n")



# convert a string to morse code
phrase= ""
for word in a:
        for i,j in zip(codes.keys(),codes.values()):
                if word.upper() == i:
                        phrase= phrase + j
                        print(i)
                        print(j)
                        break


print(phrase)


# code for reverse morse code search











