# A program to count the number of upper-case alphabets present in a text file "article.txt".

count = 0
file = open("article.txt","r")
sentenceObj = file.read()
for index in range(len(sentenceObj)):
    if sentenceObj[index].isupper():
        count += 1

print("Number of upper-case alphabets are: ",count)
file.close()