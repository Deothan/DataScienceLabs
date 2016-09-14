import re
from Lab_2 import CSVReader

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

#Not sorting ot everything
def standardizeHeight( entries ):
    for item in entries:
        if "'" in item.height:
            split = item.height.split("'");
            feet = split[0]
            inch = split[1]
            item.height = str(float(re.sub('[^0-9]','', feet))*12 + float(re.sub('[^0-9]','', inch)))
            print(item)
    return entries

list = CSVReader.CSVReader().readData()
print(len(list))

list = removeEmptyEntries(list)
print(len(list))

list = standardizeGender(list)
print(len(list))

list = standardizeHeight(list)
for item in list:
    print(item)
