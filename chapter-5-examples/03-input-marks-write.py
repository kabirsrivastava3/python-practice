#Get roll numbers, name & marks of the students of a class(get from user) and store these details in a file- marks.txt

count = int(input("How many students are there in class? "))
fileObj = open('marks.txt',"w")

for i in range(count):
    print("Enter details for student",(i+1),"below:")
    rollNo = int(input("Rollno: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    records = str(rollNo) + "," + name + "," + str(marks) + '\n'
    fileObj.write(records)
fileObj.close()