#read and display the contents of Employee.csv in 23-a

import csv
with open('compresult.csv',"r") as fhObj:
    cReader = csv.reader(fhObj)
    for rec in cReader:
        print(rec)
