# To count and display the number of lines starting with alphabet 'A' present in a text file " LINES.TXT". e.g., the file "LINES.TXT" contains the following lines:
# A boy is playing there.
# There is a playground.
# An aeroplane is in the sky.
# Alphabets & numbers are allowed in password.
# The function should display the output as 3.

count = 0 
file = open("lines.txt","r")

listObj = file.readlines()
for index in listObj :
    if index[0] == "A":
        print(index)
        count  += 1
print("Number of sentences started with A: ",count)
        
file.close()
