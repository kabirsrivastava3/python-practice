# Program to read a given CSV file having tab delimiter.

import csv
file = open("poem.txt","r" )
data = csv.reader(file, delimiter = "|")
for index in data :
      print(index)

file.close()


