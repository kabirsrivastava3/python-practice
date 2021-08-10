#update records of students > 81 marks,+2 bonus marks

import pickle
stu = {}  #declare empty dictionary object; it will hold record
found = False
print("Searching in file Stu.dat")
#open binary file in read mode and process with the with block 
finObj = open('Stu.dat',"rb+")
#read from the file
try:
    while True:
        rpos = finObj.tell()
        stu = pickle.load(finObj)
        if stu['Marks'] > 81:
            stu['Marks']+=2
            finObj.seek(rpos)
            pickle.dump(stu,finObj)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching record found.")
    else:
        print("Record(s) successfully updated.")




