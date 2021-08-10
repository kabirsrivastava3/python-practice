# dictionary COMPANY, a method to search and display the content in a pickled file COMPANY.DAT, where CompID key of the dictionary is matching with the value '1005'.
# Company = {'CompID' = ____, 'CName' = ____, ‘Turnover’ = ____}

import pickle

file = open("company.dat","rb")
found = 0
try :
      while True :
            Company = pickle.load(file)
            if Company["CompID"] == '1005':
                  print(Company)
                  found=1
            
except EOFError :
      if found == 0:
            print("Not found!!!")     

file.close()

