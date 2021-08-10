#sum  of numbers of a list using recursion

def sumOfList(number, size):
    if size == 0:
        return number[0]
    else:
        return number[size] + sumOfList(number,size-1)

numberList = [10,20,30,40,50]
length = len(numberList)

print("Sum = ",sumOfList(numberList,length-1))
