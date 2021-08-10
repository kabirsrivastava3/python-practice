#Add the GIVEN elements of list 1 and 2 to list 3 and print list 3.

def mergeLists(list1,list2,list3):
    list3.extend(list1)
    list3.extend(list2)
    return list3

list1 = ['a','b','c']
list2 = ['h','i','t']
list3 = ['0','1','2']
output= mergeLists(list1,list2,list3)
print(output)