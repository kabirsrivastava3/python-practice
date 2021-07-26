





for row in range(10):
    if row >= 5:
        print ("*" * 5)
    elif row <= 5 :
        for column in range(5):
            if column == 4 :
                print ("*" * 5)
            else :
                print(" ",end=" ")
    print(" ")