#A program that counts the number of characters up to the first $ in a text file.

file = open("poem.txt","r")

data = file.readlines()

for index in range(len(data)):
      for secondIndex in range(len(data[index])):
            if data[index][secondIndex] == "$":
                  break

print( "Total number of characters up to the first $ are = ",(index+secondIndex))
file.close()
