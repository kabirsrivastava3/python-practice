


n = int(input("Enter the limit: "))

for row in range(n,0,-1):
    for column in range(row,0,-1):
        print("*",end=" ")
    for column in range(2*(n - row)):
        print(" ",end=" ")
    for column in range(row,0,-1):
        print("*",end=" ")
    
    print()
for row in range(n):
    for column in range(row + 1):
        print("*",end=" ")
    for column in range(2*(n - row - 1)):
        print(" ",end=" ")
    for column in range(row + 1):
        print("*",end=" ")
    
    print()
