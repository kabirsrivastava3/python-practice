# A program to write a nested Python list to a csv file in one go. After writing the CSV read the CSV file and display the content.

import csv

file = open("nestedList.txt","r+")
listObj = eval(input("Enter a nested list: "))
fileWrite = csv.writer(file)
fileWrite.writerows(listObj)

data = csv.reader(file)
for index in data :
      print(index)

file.close()
