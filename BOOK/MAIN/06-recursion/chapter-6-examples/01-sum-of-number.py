#sum of number using recursion

def sum(number):
    if number == 1:
        return 1
    else:
        return(number + sum(number-1))

print("Enter the limit of sum required: ")
number = int(input())

print(sum(number))

