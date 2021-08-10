#print a sentence
#print: No. of words
#print: No. of characters
#print: Percentage of alpha-numeric characters

#Time Complexity = O(N)

sentence = input("Enter a sentence = ")
print(sentence)
length = len(sentence)
countWords = 1
alphaNumeric = 0 
for search in sentence:
    if search == " " :
        countWords += 1
    elif search.isalnum():
        alphaNumeric += 1
percentAlpha = (alphaNumeric/length)*100
print("Number of Words are: ",countWords)
print("number of Characters are: ",length)
print("Percentage of Characters that are Alpha-Numeric: ",percentAlpha)
