#printing a string backwards using Recursion

def reverseStringRecursion(sentence,length):
    if length == 0:
        print(sentence[0])
    if length > 0:
        print(sentence[length],end ="")
        return reverseStringRecursion(sentence,length-1)

print("Enter a string: ")
inputString = input()
size = len(inputString)
print("Reverse of String",inputString,"is",reverseStringRecursion(inputString,size-1))
