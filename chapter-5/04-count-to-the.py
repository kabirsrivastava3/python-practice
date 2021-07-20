#A program to count the words "to" and "the" present in a text file "poem.txt". 

countTo = 0
countThe = 0
file = open("poem.txt", "r")
listObj = file.readlines()

for index in listObj:
    word = index.split()
    for search in word:
        if search == "to":
            countTo += 1
        elif search == "the":
            countThe  += 1

print("Number of 'to': " ,countTo)
print("Number of 'the': " ,countThe)

file.close()
