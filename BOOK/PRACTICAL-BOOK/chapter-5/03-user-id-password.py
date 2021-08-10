# A program that asks a new user about userid and password and then appends it to file “security. txt” provided the give userid does not exist in the file . 
# If it does, then display error message “User id already exist”and prompt the user to re-enter the userid. 
# Also, make sure that the password is a least 8 characters long with at least a digit and a special character out of “$, @and %” in it.


def password():
    inputPassword= input ("Enter the password :- ")
    if len(inputPassword) >= 8 and ("$" in inputPassword or "@" in inputPassword or "%" in inputPassword):
        print ("Done")
        fileObj.write(userid ," ", inputPassword , "\n")
    else :
        print ("Re-enter the password")
        password()
        
fileObj = open("security.txt","r+")
text = fileObj.readlines()
userid = input("Enter User-ID: ")
same = 0
for index in text:
    line = index.split()
    if line[0] == userid:
        same = 1
        print("User-ID already exists")
if same == 0:
    password()

fileObj.close()

 