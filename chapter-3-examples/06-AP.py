


def AP(intialValue,step):
    return intialValue, intialValue + step, intialValue + 2 * step,intialValue + 3 * step

  

initialValue = int(input("Enter Initial Value: "))
step = int(input("Enter Step: "))


term1,term2,term3,term4 = AP(initialValue, step)

print(term1,term2,term3,term4)
