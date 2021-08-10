# A program that reads a text file and creates another file that is identical except that every sequence of consecutive blank spaces is replaced by a single space.


file1 = open("poem.txt","r")
file2 = open("newPoem.txt","w")

listObj = file1.readlines()

for index in listObj:
    word = index.split()
    file2.write(" ".join(word))
    file2.write("\n")

print("Program has successfully run")

file2.close()
file1.close()




