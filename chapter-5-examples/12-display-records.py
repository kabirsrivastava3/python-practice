# display records

import pickle
stu = {}  #declare empty dictionary object; it will hold record
finObj = open('Stu.dat',"rb") #open binary file in read mode
#read from the file
try:
    print("File Stu.dat store these records")
    while True: #it will become False upon EOF.
        stu = pickle.load(finObj) #read record in stu dictionary fron finObj file handle
        print(stu) #print the read record

except EOFError:
    finObj.close() #close file