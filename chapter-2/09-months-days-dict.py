#Create a dictionary whose keys are month name and whose values are number of days:

#(a) ask the user to enter the month name and use the dictionary to tell how many days are in month.
#(b) print out all of the keys in alphabetical order.
#(c) print out all of the month with 31 days
#(d) print out the (key - value) pair sorted  by the number of the days in each month.


month = {"January":31, "February":28, "Leap February":29, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31 , "November":30, "December":31}

mon = input("Enter the month name = ")
print("Number of days in ",mon, "=", month[mon])

monthList = list(month.keys())
monthList.sort()

print(monthList)
print("Months which have 31 days: ")

for i in month:
    if month [i] == 31:
        print(i)

print("Months according to number of days: ")
print("February")

for i in month:
    if month [i] == 30:
        print(i)

for i in month:
    if month [i] == 31:
        print(i)
