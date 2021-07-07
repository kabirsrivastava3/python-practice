def modifiedLinearSearch():
    info = {"Riya":"Csc.", "Mark":"Eco", "Ishpreet":"Eng", "Kamaal":"Env. Sc"}
    element = input("Enter the element to be searched for: ")
    for search in info:
        if info[search].upper()== element.upper():
            print("The key of given value is: ",search)
            break
    else:
        print("Given value does not exist in dictionary")
    
    return

modifiedLinearSearch()

