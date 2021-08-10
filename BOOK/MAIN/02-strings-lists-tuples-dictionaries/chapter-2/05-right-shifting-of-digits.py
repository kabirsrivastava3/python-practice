#Rotate the elements of a list to the right by 1.
#Time Complexity = O(N*N)


def rightShiftArray():
    numList=[]
    numValue = 0
    size = int(input("Enter the size of lists: "))
    
    for index in range(size):
        numValue = int(input("Enter the numbers in list: "))
        numList.append(numValue)

    print("The Original Array is: ",numList)
    rotate = int(input("How many times you want to rotate the array? ")) #rotate = 1
    for count in range(rotate):
        temporaryVariable = numList[size-1]
        for index in range(size-2,-1,-1):
            numList[index+1] = numList[index]
        numList[0] = temporaryVariable
    
    print("List after rotating right",rotate,"times is:",numList)

rightShiftArray()