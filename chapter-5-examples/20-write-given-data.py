#write given data in a file:

# ['Name','Points','Rank'],
#   ['Shradha',4500,23],
#   ['Nischay',4800,31],
#   ['Ali',4500,25],
#   ['Adi',5100,14]

import csv
fhObj = open("compresult.csv","w") #open file
cwriter = csv.writer(fhObj)
compData = [
    ['Name','Points','Rank'],
    ['Shradha',4500,23],
    ['Nischay',4800,31],
    ['Ali',4500,25],
    ['Adi',5100,14]]
cwriter.writerows(compData)
fhObj.close()