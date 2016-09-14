import csv
import re

class Data:

    def __init__(self, time, gender, height):
        self.time = time
        self.gender = gender
        self.height = height

    def __str__(self):
        return self.time + " " + self.gender + " " + self.height

def readData():
    list = []
    file = open("heights_raw.csv", newline="")
    reader = csv.reader(file)

    for row in reader:
        list.append(Data(row[0], row[1], row[2]))

    return list

def removeEmptyEntries( entries ):
    for item in entries:
        if item.time == "" or item.gender == "" or item.height == "":
            del entries[entries.index(item)]
    return entries

def standardizeGender( entries ):
    for item in entries:
        if item.gender.lower() != "male" and item.gender.lower() != "female":
            del entries[entries.index(item)]
    return entries

#at one point the split gives more than 2 outputs.
def standardizeHeight( entries ):
    for item in entries:
        if "'" in item.height:
            feet, inch = item.height.split("'")
            print(item)
            item.height = str(int(re.sub('[^0-9]','', feet))*12 + int(re.sub('[^0-9]','', inch)))
            print(item)
    return entries

list = readData()
print(len(list))

list = removeEmptyEntries(list)
print(len(list))

list = standardizeGender(list)
print(len(list))

list = standardizeHeight(list)
#for item in list:
    #print(item)
