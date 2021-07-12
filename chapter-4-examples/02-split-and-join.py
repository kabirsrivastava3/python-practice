#encryption/decryption using split() and join()

def encrypt(sentence,key):
    return key.join(sentence)

def decrypt(sentence,key):
    return sentence.split(key)

#_main_
print("Enter a sentence: ")
sentence = input("")

print("Enter an encrytion key: ")
key= input("")

encryptString = encrypt(sentence,key)
decryptList = decrypt(encryptString,key)

decryptString = "".join(decryptList)

print("String after Encryption is: ",encryptString)
print("String after Decryption is: ",decryptString)


#---------------------------------------------------
#<str>.join()

#print("*".join("Hello")) 
#H*e*l*l*o
#print("***".join("TRIAL")) 
#T***R***I***A***L

#print("$$".join(["trial","hello"]))
#trial$$hello

#print("$$".join(("trial","hello","new")))
#trial$$hello$$new

#print("$$".join((123,"hello","new")))
#error

#---------------------------------------------------
#<str>.split()

#print("I love Python".split())
#['I', 'love', 'Python']

#print("I love Python".split("o"))
#['I l', 've Pyth', 'n']
