# get data to write onto the file as long as user wants

import pickle
stu = {}
stuObj = open('Stu.dat',"wb")
#get data to write onto the file
answer = 'y'
while answer == 'y':
    rollno = int(input("Rollno: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    #add read data into dictionary
    stu['Rollno'] = rollno
    stu['Name'] = name
    stu['Marks'] = marks
    # now write into the file
    pickle.dump(stu,stuObj)
    answer = input("Want to enter more records? (y/n)...")
stuObj.close() #close the file
