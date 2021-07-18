# Read a file by line & display each word separated by a '#' 

fileObjNew = open('answer.txt',"a+")
line = ""
while line:
    line = fileObjNew.readline()
    #printing the line word by word using split()
    for word in line.split():
        print(word, end='#')
    print()
#close the file
fileObjNew.close()