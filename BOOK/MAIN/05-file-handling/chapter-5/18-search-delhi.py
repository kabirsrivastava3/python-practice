# A function in to search and display details of all trains, whose destination is Delhi from a binary file TRAIN.DAT. 
# Assuming the binary file is containing the objects of the following dictionary type:
# Train = { 'Tno': ___, ‘From’: ____, 'To' : ____}

import pickle

def searchTrain() :
      file = open("train.dat","rb")
      found = 0
      try :
            while True :
                  Train = pickle.load(file)
                  if Train["To"] == 'Delhi':
                        print(Train)
                        found=1
            
      except EOFError :
            if found == 0:
                  print("Not found!!!")     

      file.close()

searchTrain()
