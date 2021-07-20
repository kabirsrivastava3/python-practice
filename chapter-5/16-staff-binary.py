# Consider the following definition of dictionary Staff, 
# Search and display the content in a pickled file staff.dat, where Staffcode key of the dictionary is matching with 'S0105'.
# Staff = {‘Staff Code': _____, 'Name' = _____}

import pickle
file = open("staff.dat", "rb")
found = 0
try :
    while True :
            staff = pickle.load(file)
            if staff ["Staff Code"] == 'S0105':
                  print(staff)
                  found=1
            
except EOFError :
      if found == 0:
            print("Not found!!!")     

file.close()
