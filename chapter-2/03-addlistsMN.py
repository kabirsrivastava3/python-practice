#Input two lists L and N of same size. 
#Add their elements in a new list P
#Print the new list
    
size = int(input("Enter the size of lists: "))
L=[]
N=[]
for index in range(size):
    valueM = int(input("Enter the numbers in list L: "))
    L.append(valueM)
for index in range(size):
    valueN = int(input("Enter the numbers in list N: "))
    N.append(valueN)
P = []
for index in range(size):
    P = P + [L[index] + N[index]]
print("New List = ",P)
