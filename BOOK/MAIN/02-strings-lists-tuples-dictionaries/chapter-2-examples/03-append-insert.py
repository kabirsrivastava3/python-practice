#Add the GIVEN elements of list 2 and insert the elements of list 3 to list 1.

def operationLists(list1,list2,list3):
    list1.append(list2)
    list1.insert(0,list3)
    return list1

list1 = ['a','b','c']
list2 = ['h','i','t']
list3 = ['0','1','2']
output=operationLists(list1,list2,list3)
print(output)
