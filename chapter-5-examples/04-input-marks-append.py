# Add 2 more records to marks.txt

fileObj = open('marks.txt',"a")

for i in range(2):
    print("Enter details for student",(i+1),"below:")
    rollno = int(input("Rollno: "))
    name = input("Name: ")
    marks = float(input("Marks: "))
    records = str(rollno) + "," + name + "," + str(marks) + '\n'
    fileObj.write(records)
fileObj.close()