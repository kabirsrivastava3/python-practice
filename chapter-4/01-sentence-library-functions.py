#1)remove_letter(sentence, letter) 
#For example: remove_letter("Hello there!","e") should return the string "Hllo thr!". 
#Try implementing it using <str>.split() function.
#2) Try implementing the capwords () functionality using other functions, i.e , split(), capitalize () and join( ). 
#Compare the result with the capwords() function's result.

import string


def removeLetter(sentence,letter):
    newSentence = ""
    splitSentence = sentence.split(letter)
    for index in splitSentence:
        newSentence += index
    return newSentence


print(removeLetter("Hello there!","e"))

def capWords(line):
    print(line.split())
    print(line.capitalize())
    print("+".join(line))
    print(string.capwords(line))
    
print("Enter a sentence: ")
str = input() 
print(capWords(str))