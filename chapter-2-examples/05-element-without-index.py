#find an element's index/position in a tuple WITHOUT using index()

def input(char):
    return char

def checkTuple(tupleN,charN):
    if charN in tupleN:
        count = 0
    for element in tuple1:
        if element != charN:
            count+=1
        else:
            break
    return count

find = input('e')
print(find)
tuple1 = ('a','p','p','l','e')
output = checkTuple(tuple1,find)
print(output)
