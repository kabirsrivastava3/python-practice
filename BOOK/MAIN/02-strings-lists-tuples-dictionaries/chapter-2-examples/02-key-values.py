# inputting and printing the key and values of a dictionary from a user.
#Time Complexity = O(N)

def input(total):
    return total

def inputDict(total):
    compWinners = {}
    for element in range(total):
        key = input("How many students? ")
        value = input("How many students? ")
        compWinners[key] = value

    return compWinners

find=input(5)
output=inputDict(find)
print(output)

