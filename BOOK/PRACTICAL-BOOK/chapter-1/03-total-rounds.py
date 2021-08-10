# An athlete is taking rounds of a triangular park with sides as 30 m, 25 m and 35 m . 
# The athlete has run 560 m till now. 
# Print how many rounds of park the athlete has completed.

def totalRounds():
    side1 = 30
    side2 = 25
    side3 = 35
    distance = 560
    perimeter = side1 + side2 + side3

    rounds = distance // perimeter
    print("Rounds completed by athlete is:",rounds)

totalRounds() 
