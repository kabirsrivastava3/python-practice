#random number generator that generates between 1 and 6(a dice)

import random

low = 1
high = 6
rollAgain = 'y' 

while rollAgain == 'y' or rollAgain == 'Y':
    print("Rolling the dice..")
    val = random.randint(low,high)
    print("You get..",val)
    rollAgain = input("Roll the dice again?(y/n)...")

