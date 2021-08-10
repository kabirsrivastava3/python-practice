#Enter day in a year from 2 to 365 and print the corresponding day according to day

inputDayNumber = int(input("Enter day number between 2 & 365 : "))
day = input("Enter first day of the year :  ")
listOfDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(listOfDays[listOfDays.index(day) + inputDayNumber%7 - 1])

#index()	Returns the index of the first element with the specified value