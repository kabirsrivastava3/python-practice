def sentenceOperations():
    sentence = input("Enter a sentence: ")
    uppercount = 0
    lowercount = 0
    digitcount = 0
    alphacount = 0

    for check in sentence:
        if check.isupper():
            uppercount+=1
        elif check.islower():
            lowercount+=1
        elif check.isdigit():
            digitcount+=1     
        if check.isalpha():
            alphacount+=1
    
    print("Number of Uppercase Letters " + str(uppercount))
    print("Number of Lowercase Letters "+str(lowercount))
    print("Number of Digits "+str(digitcount))
    print("Number of Alphabets "+str(alphacount))

sentenceOperations()