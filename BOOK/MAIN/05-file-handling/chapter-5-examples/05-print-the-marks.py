# Print the total records 

fileObj = open('marks.txt',"r")
while str:
    str = fileObj.readline()
    print(str,end="")
fileObj.close()