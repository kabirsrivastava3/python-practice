# Consider the following definition of dictionary Member, 
# Write a method in python to write the content in a pickled file member.dat.
# Member = {'MemberNo.': _____, 'Name': _____}

import pickle

file = open("member.dat","wb")

while True :
      memberDict={}
      memberNo = int(input("Enter MemberNo. :"))
      name = input("Enter Name: ")
      memberDict["MemberNo."] = memberNo
      memberDict["Name"] = name
      pickle.dump( memberDict, file )
      user = input("For exit: type quit: ")
      if user == "quit":
            break
print("Thankyou")

file.close()
