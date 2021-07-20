# A function that reads a csv file and creates another csv file with the same content, but with a different delimiter.

import csv

file1 = open("new.txt","r")
data = csv.reader(file1)

file2 = open( "old.txt","w",newline=" ")
fileWrite = csv.writer(file2, delimiter = "|")
fileWrite.writerows(data) 

file2.close()
