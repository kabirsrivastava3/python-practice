# A program that accepts a list and removes the value at index 0 from the list.


def removeElementArray():
    numList = []
    size = int(input("Enter the size of the array: "))
    numValue = 0

    for index in range(size):
        numValue = int(input("Enter the number: "))
        numList.append(numValue)

    numList.pop(0)
    print(numList)

removeElementArray()