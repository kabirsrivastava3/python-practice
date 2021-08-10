#create a list of integers < 100 that are multiples of 3 and 5
#Time Complexity = O(N)

numList = []

for index in range (1,100):

    if index % 3 == 0 or index % 5 == 0 :
        numList.append(index)

print (numList)