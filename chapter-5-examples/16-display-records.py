#Display records of students > 81 marks

import pickle
stu = {}  #declare empty dictionary object; it will hold record
found = False
print("Searching in file Stu.dat")
#open binary file in read mode and process with the with block 
with open('Stu.dat',"rb") as finObj:
    stu = pickle.load(finObj) #read record in stu dictionary fron finObj file handle
    if stu['Rollno'] > 81:
            print(stu) #print the record
            found = True
    if found == False:
        print("No such records found in the file")
    else:
        print("Search successful.")
