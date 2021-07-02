def  timeDifference():
    firstTime = int(input("Enter the first time = "))
    secondTime = int(input("Enter the second time = "))
    timeDiff = secondTime - firstTime
    print (timeDiff // 100, "hours " , timeDiff % 100, "min")

    return None

timeDifference()