# A program that reverses a 2D array of integers, implemented as nested list, in the order of 0th element of every inner list.


nestedList = [[1,2,3],[4,5,6],[7,8,9]]

for index in range(len(nestedList)):
    nestedList[index].reverse()

print(nestedList)


