# blank lines are not displayed

import csv
with open('compresult.csv',"r",newline='\r\n') as fhObj:
    cReader = csv.reader(fhObj)
    for rec in cReader:
        print(rec)
