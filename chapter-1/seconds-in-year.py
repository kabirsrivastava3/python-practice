def secondsInYear():
    inputYear = int(input("Enter a year: "))
    totalSeconds = inputYear * 365 * 24 * 60 * 60  #seconds in a year

    print(str(inputYear)+" in seconds = "+str(totalSeconds)+" seconds")

    return None

secondsInYear()
   