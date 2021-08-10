#Rotate the elements of a list to the left by 2.


def leftShiftArray():
    numList = []
    size = int(input("Enter the size of the list: "))
    numValue = 0
    for number in range(size):
        numValue = int(input("Enter the element: "))
        numList.append(numValue)
    
    print("Original Array is:",numList)
    rotate = int(input("How many times you want to rotate the list? ")) # rotate = 2
    for count in range(rotate):
        temporaryVariable = numList[0]
        for index in range(1,size):
            numList[index-1] = numList[index]
        numList[size-1] = temporaryVariable
    
    print("List after shifting left",rotate,"number of times is: ",numList)


leftShiftArray()





    
