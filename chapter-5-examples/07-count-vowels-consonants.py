

fileObj = open('answer.txt',"r")
ch = ""
vCount = 0
cCount = 0
while ch:
    ch = fileObj.read(1) #one character read from file
    if ch in ['A','a','E','e','I','i','O','o','U','u']:
        vCount+=1
    else:
        cCount+=1
    print("Vowels in the file: ", vCount)
    print("Consonants in the file: ",cCount)
#close the file
fileObj.close()