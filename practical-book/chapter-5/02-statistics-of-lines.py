# A program to print following type of statics for the given file:

#   16824  line in the file
#     438   empty lines
#    53.7  average characters per line
#    65.9  average characters per non – empty line


fileObj = open("sarojiniPoem.txt","r")
text = fileObj.readlines()
fileObj.seek(0,0)
characters = fileObj.read()
fileObj.close()
totalCharacters = len(characters)
totalLines = 0
emptyLines = 0
for line in text:
    totalLines += 1
    if line.isspace() == True:
        emptyLines += 1

averageEmpty = round((totalCharacters/totalLines),1)
averageNonEmpty = round((totalCharacters/(totalLines - emptyLines)),1)

print(totalLines,"lines in the file")
print(emptyLines,"empty lines")
print(averageEmpty,"average characters per line")
print(averageNonEmpty,"average characters per non – empty line")

