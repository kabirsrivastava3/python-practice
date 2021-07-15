#Neon Number
#A neon number is a number where the sum of digits of square of the number is equal to the number. The task is to check neon number.
#Input : 9
#Output : Neon Number
#Explanation: square is 9*9 = 81 and sum of the digits of the square is 9.

import math
def square(n):
  square = math.pow(n,2)
  
  return square

def sumOfDigits(number):
  sum=0
  while number != 0:
    remainder = number %10
    sum = sum + remainder
    number = math.floor(number/10)
  
  return sum

def neonNumber(num):
  S = square(num)
  sod = sumOfDigits(num)
  return (sod == num)

neonNumber(9)

