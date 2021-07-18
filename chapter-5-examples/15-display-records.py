#display records of students of roll no. 22 and 23.

import pickle
stu = {}  #declare empty dictionary object; it will hold record
found = False
finObj = open('Stu.dat',"rb") #open binary file in read mode
searchKeys = [22,23]
#read from the file
try:
    print("File Stu.dat store these records")
    while True: #it will become False upon EOF Exception.
        stu = pickle.load(finObj) #read record in stu dictionary fron finObj file handle
        if stu['Rollno'] in searchKeys:
            print(stu) #print the record
            found = True

except EOFError:
    if found == False:
        print("No such records found in the file")
    else:
        print("Search successful.")
finObj.close() #close file

