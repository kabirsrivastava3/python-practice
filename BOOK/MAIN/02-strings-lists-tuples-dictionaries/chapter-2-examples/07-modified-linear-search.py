#fixed case sensative for finding and priting key
#Time Complexity = O(N)

def input(element):
    return element

def findValue(inform,key):
    for search in inform:
        return inform[search].upper()== key.upper()

find = input("Ishpreet")
print(find)
info = {"Riya":"Csc.", "Mark":"Eco", "Ishpreet":"Eng", "Kamaal":"Env. Sc"}
output = findValue(info,find)
print(output)

