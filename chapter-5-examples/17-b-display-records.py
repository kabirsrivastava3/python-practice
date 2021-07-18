#display records

import pickle
stu = {}  #declare empty dictionary object; it will hold record
finObj = open('Stu.dat',"rb")
try:
    while True:
        stu = pickle.load(finObj) #read record in stu dictionary from fin
        print(stu) #print the read record
except EOFError:
    finObj.close()       #close the file