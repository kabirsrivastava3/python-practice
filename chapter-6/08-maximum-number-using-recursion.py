#Maximum Number in a List using Recursion


def maxUsingRecursion(maximum,numArray,index):
    if index == len(numArray):
        print(maximum)
    elif maximum < numArray[index]:
        maximum = numArray[index]
        return maxUsingRecursion(maximum,numArray,index+1)
    else :
        return maxUsingRecursion(maximum ,numArray,index+1)


size = int(input("Enter the size of the list: "))
numList=[]
for index in range(size):
    valueNL = int(input("Enter the numbers in the list: "))
    numList.append(valueNL)
      
maxUsingRecursion(numList[0],numList,1)