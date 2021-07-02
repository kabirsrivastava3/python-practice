def checkVariable():
    x = int(input("Enter a number: "))
    if x < 0:
        print("Negative")
    elif x == 0:
        print("Zero")
    elif x > 0:
        print("Positive")
    
    return -1 

checkVariable()