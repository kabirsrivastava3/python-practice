# create a csv file by supressing the EOL translation

import csv
fhObj = open("Employee.csv","w",newline="") #open file
cwriter = csv.writer(fhObj)
empData = [
    ['Empno','Name','Designation','Salary'],
    ['1001','Trupti','Manager',56000],
    ['1002','Raziya','Manager',55900],
    ['1003','Simran','Analyst',35000],
    ['1004','Silviya','Clerk',31000],
    ['1005','Suji','PR Officer',31000]]
cwriter.writerows(empData)
print("Files successfully created.")
fhObj.close()