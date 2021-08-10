#Input  5 records in a CSV file

import csv
fhObj = open("Student.csv","w") #open file
stuwriter = csv.writer(fhObj)
stuwriter.writerow(['Rollno', 'Name', 'Marks'])

for i in range(5):
    print("Student record", (i+1))
    rollno = int(input("Enter Rollno: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    sturec = [rollno, name, marks]
    stuwriter.writerow(sturec)
fhObj.close()