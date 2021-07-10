#Rotate the elements of a list to the right by 1.
#Time Complexity = O(N*N)

size = int(input("Enter the size of lists: "))
numList=[]
for index in range(size):
    valueNumList = int(input("Enter the numbers in list: "))
    numList.append(valueNumList)

rotate = 2
for i in range(rotate):
    temp = numList[size-1]
    for index in range(size-1,0,-1):
        numList[index] = numList[index-1]

    numList[0] = temp

print("Shifted array is: ",numList)


