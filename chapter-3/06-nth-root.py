#A function - nthRoot () -two parameters x and n and returns nth root of x i.e., X**1/n . 
# The default value of n is 2.


def nthRoot(x,n=2):

    return x ** (1/n)


#For Default value:
print(nthRoot(1))

#For provided value:
print(nthRoot(8,3))
