#read and display the contents of Employee.csv in 23-a

import csv
with open('Employee.csv',"r") as fhObj:
    eReader = csv.reader(fhObj)
    print("File Employee.csv contains :")
    for rec in eReader:
        print(rec)
