#A file contains a list of telephone numbers in the following form:
#1) Arvind 7258031
#2) Sachin 7259197.
#The names contain only one word the names and telephone numbers are separated by white spaces. 
#Program to read a file and display its contents in two columns. 

print("Name      |                  Phone no. ")

newFile = open("telephone.txt", "r")

listObj = newFile.readlines()

for index in listObj:
    data = index.split()
    print( data[0], end = "\t")
    print("|", end = "\t")
    print(data[1])

newFile.close()
