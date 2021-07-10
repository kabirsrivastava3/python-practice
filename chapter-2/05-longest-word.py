#longest word in a list
#Time Complexity = O(N)

wordList = []

size = int(input("Enter the size of list: "))

for index in range(size):
    valueWL = (input("Enter the words in list : "))
    wordList.append(valueWL)

long =  len(wordList[0])

for listElement in wordList:
    print(listElement)
    if long <= len(listElement):
        long = len(listElement)
        word = index

print ("Longest word in the list is: ", word)
