#inputting a sentence and counting no. of uppercase, lowercase, digits and alphabets in it.
#Time Complexity = O(N)

def input(sentence):
    return sentence

def checkFunctions(sentence):
    upperCount = 0
    lowerCount = 0
    digitCount = 0
    alphaCount = 0
    for check in sentence:
        if check.isupper():
            upperCount+=1
        elif check.islower():
            lowerCount+=1
        elif check.isdigit():
            digitCount+=1     
    if check.isalpha():
        alphaCount+=1
    
    print("Number of Uppercase Letters " + str(upperCount))
    print("Number of Lowercase Letters "+str(lowerCount))
    print("Number of Digits "+str(digitCount))
    print("Number of Alphabets "+str(alphaCount))

find = input("fi6780YUIBBWLLW LKkKMMmmlhvw68")
checkFunctions(find)
