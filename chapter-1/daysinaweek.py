#index()	Returns the index of the first element with the specified value

def daysInAweek():
    inputDayNumber = int(input("Enter day number between 2 & 365 : "))
    day = input("Enter first day of the year :  ")
    listofdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(listofdays[listofdays.index(day) + inputDayNumber%7 - 1])

    return

daysInAweek() 
