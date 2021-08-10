#Read Emp.dat and display it

import pickle
#declare empty dictionary object; it will hold record
emp = {}
empObj = open('Emp.dat',"rb") #open binary file in read mode
#read from the file
try:
    while True: #it will become False when the end of the file is reached(EOF Exception).
        emp = pickle.load(empObj) 
        print(emp)

except EOFError:
    empObj.close() #close file

