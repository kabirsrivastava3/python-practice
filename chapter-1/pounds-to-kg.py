#The format() method formats the specified value(s) and insert them inside the string's placeholder.
#The placeholder is defined using curly brackets: {}.

def poundsToKg():
    print("Pounds |  Kgs")
    for convert in range(1,10):
        print("{}  |  {}".format(convert,convert*0.45))
    
    return None

poundsToKg()