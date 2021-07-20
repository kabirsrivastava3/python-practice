# A file sports.dat contains information in following format :
#Event ~ Participant
#A function that would read contents from file sports.dat and creates a file named Atheletic.dat copying only those records from sports.dat where the event name is " Atheletics ".


def  eventParticipant():
    file1 = open("sports.txt","r")
    file2 = open("Atheletics.txt","w")
    listObj = file1.readlines()
    for index in listObj:
        print(index[:9])
        if index[:9] == "atheletic" or index[:9] == "Atheletic":
            file2.write(index)
            
    file1.close()
    file2.close()
    
eventParticipant()





