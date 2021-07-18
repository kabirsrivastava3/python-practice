# write dictionary objects to be stored in a binary file


import pickle
#dictionary objects to be stored in a binary file
emp1 = {"Empno" : 1201, "Name" : "Anushree", "Age" : 25, "Salary" : 47000}
emp2 = {"Empno" : 1211, "Name" : "Zoya", "Age" : 30, "Salary" : 48000}
emp3 = {"Empno" : 1251, "Name" : "Simarjeet", "Age" : 27, "Salary" : 49000}
emp4 = {"Empno" : 1266, "Name" : "Alex", "Age" : 29, "Salary" : 50000}

empObj = open('Emp.dat',"wb")

#write onto the file

pickle.dump(emp1,empObj)
pickle.dump(emp2,empObj)
pickle.dump(emp3,empObj)
pickle.dump(emp4,empObj)

print("Successfully written four dictionaries")
empObj.close()
