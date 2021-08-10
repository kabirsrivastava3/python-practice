# A function that takes a character and returns true if it is a vowel, false otherwise.


def vowel(character):
    if character == "a" or character =="e" or character =="i" or character == "o" or character =="u" or character =="A" or character =="E" or character == "I" or character =="O" or character =="U":
        return True
    else:
        return False
inputCharacter = input("Enter the letter: ")
print(vowel(inputCharacter))
