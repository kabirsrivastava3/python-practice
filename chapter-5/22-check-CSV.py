#A function that reads a csv file and creates another csv file with the same content except the lines beginning with 'check'.

import csv
file1 = open( "new.txt","r")
file2 = open( "new2.txt","w",newline=" ")
fileWrite = csv.writer( file2 , delimiter = "|")

data = csv.reader(file1)

for index in data :
      fileWrite.writerow(["Check"] + index) 

file2.close()
