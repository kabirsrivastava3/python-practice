#input a date in int and print as Month Date, Year Format

inputDate = input("Enter a date in MMDDYYYY format : ")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[int(inputDate[:2])], inputDate[2:4], ',', inputDate[5:])
    