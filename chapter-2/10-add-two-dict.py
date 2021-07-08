#create a function called addDict(dict1, dict2) = union of two dictionaries
#print a new dictionary with all the items in both its arguements

def addDict(dict1, dict2):
    newDict = {}
    for index in dict1.keys():
        newDict[index] = dict1[index]
        
    for index in dict2.keys(): 
        newDict[index] = dict2[index]
    return newDict

dict1 = {"a" : 1, "b" : 2, "c" : 3}
dict2 = {"c" : 4, "d" : 5, "e" : 6}

print(addDict(dict1, dict2))
