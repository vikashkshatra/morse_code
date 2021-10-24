
from playsound import playsound
import time

codes = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}
phrase = input("Enter your phrase: \n")

# convert a string to morse code
morse_code = ""
for word in phrase:
    for i, j in zip(codes.keys(), codes.values()):
        if word.upper() == i:
            morse_code = morse_code + j
            break

print(morse_code)
print("PLAYING SOUND")

# play sound beeep
for word in phrase:
    for i, j in zip(codes.keys(), codes.values()):
            dots = 0
            if word.upper() == i :
                for beep in j:
                        if beep == ".":
                                dots += 1
                                playsound("beep.wav")
                        else:
                                time.sleep(0.2)
