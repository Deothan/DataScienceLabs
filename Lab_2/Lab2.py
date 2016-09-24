import re
import CSVReader

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
    non_decimal = re.compile(r'[^\d.]+')
    for item in entries:
        if "'" in item.height:
            split = item.height.split("'");
            feet = split[0]
            inch = split[1]
            item.height = str(float(non_decimal.sub('', feet))*12 + float(non_decimal.sub('', inch)))
        elif "ft" in item.height or "inch" in item.height:
            split1 = item.height.split("ft");
            feet = split1[0]
            split2 = item.height.split("inches");
            inch = split2[0]
            item.height = str(float(non_decimal.sub('', feet)) * 12 + float(non_decimal.sub('', inch)))
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
