#search for key in the dictionary and print the corresponding value

def input(element):
    return element

def findValue(inform,key):
    if key in inform.values():
        for search in inform:
            return inform[search]== key
                
                

find = input("Ishpreet")
print(find)
info = {"Riya":"Csc.", "Mark":"Eco", "Ishpreet":"Eng", "Kamaal":"Env. Sc"}
output = findValue(info,find)
print(output)

