# Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT, and display those words, which are less than 4 characters.

def displayWords() :
    file = open("story.txt", "r")
    listObj = file.readlines()
    for index in listObj :
        word = index.split()
        for search in word:
            if len(search) < 4:
                print(search)

    file.close()

displayWords()



