#Rotate the elements of a list to the left by 2.


def inputArray(numList,rotate=2):
    length = len(numList)

    for index in range(rotate):
        temp = numList[0]
        for index in range(0,length-1):
            numList[index] = numList[index+1]
        
        numList[length-1] = temp
    
    print("The shifted array is: ",numList)



numList = [1,2,3,4,5]
print(inputArray(numList))
