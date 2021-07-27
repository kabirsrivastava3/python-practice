# Arrays in python are implemented through lists. 
# Write a program that sorts an array of integers in ascending order.

def sortArray():
    numList = []
    size = int(input("Enter the size of the array: "))
    numValue = 0

    for index in range(size):
        numValue = int(input("Enter the numbers in an unsorted manner: "))
        numList.append(numValue)

    numList.sort()
    print("Sorted List:=",numList)

sortArray()