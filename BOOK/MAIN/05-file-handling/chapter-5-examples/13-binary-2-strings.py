#create binary file and write 2 strings in it.

import pickle
string = "This is my first line. This is second line"

with open("myfile.info","wb") as fh:
    pickle.dump(string,fh)

print("File successfully created.")
