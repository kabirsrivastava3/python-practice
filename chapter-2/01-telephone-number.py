# check for valid phone number and display it
#Format: 017-555-1212

phoneNumber = input("enter your phone number = ")
length = len(phoneNumber)
if length == 12 and phoneNumber[:3].isdigit() and phoneNumber[3]== "-" and phoneNumber[4:7].isdigit() and phoneNumber[7]== "-" and phoneNumber[8:13].isdigit():
    print("It is vaild Phone-Number",phoneNumber)
else :
    print("It is not vaild Phone-Number")
