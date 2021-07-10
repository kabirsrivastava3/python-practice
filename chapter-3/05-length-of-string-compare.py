# function that receives two string arguments and checks whether they are same-length strings 
# (returns True in this case otherwise false).


def lengthEqual(line1,line2):
    return len(line1) == len(line2)


print("Enter the strings for comparison: ")
text1 = input("First string arguement: ")
text2 = input("Second string arguement: ")
print(lengthEqual(text1,text2))