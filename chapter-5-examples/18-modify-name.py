# Modify name of roll no. 22 as Gurnam

import pickle
stu = {}  #declare empty dictionary object; it will hold record
found = False
finObj = open('Stu.dat',"rb+")
#read from the file
try:
    while True:
        rpos = finObj.tell()
        stu = pickle.load(finObj) #read record in stu dictionary from fin
        if stu['Rollno'] == 22:
            stu['Name'] = 'Gurnam'
            finObj.seek(rpos)
            pickle.dump(stu,finObj)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching record found.")
    else:
        print("Record(s) successfully updated.")
finObj.close()       #close the file