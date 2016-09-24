import pandas as pd
import re

def standardizeHeight( item ):
    non_decimal = re.compile(r'[^\d.]+')
    if "'" in item:
        split = item.split("'");
        feet = split[0]
        inch = split[1]
        item = str(float(non_decimal.sub('', feet))*12 + float(non_decimal.sub('', inch)))
    elif "ft" in item or "inch" in item:
        split1 = item.split("ft");
        feet = split1[0]
        split2 = item.split("inches");
        inch = split2[0]
        item = str(float(non_decimal.sub('', feet)) * 12 + float(non_decimal.sub('', inch)))
    elif "." in item:
        split = item.split(".")
        if int(split[0]) < 10:
            item = str(int(split[0]) * 12 + int(split[1]))
    return item

#Loads the CSV file and changes the names of the rows
heights = pd.read_csv('heights_raw.csv')
heights.columns = ['Time', 'Gender', 'Height']
print(len(heights))

#Removes entries with empty values
heights = heights.dropna()
print(len(heights))

#Removes entries which are not Male or Female
heights = heights.loc[(heights["Gender"] == "Female") | (heights["Gender"] == "Male")]
print(len(heights))

#Format the Heights
heights["Height"] = heights["Height"].apply(lambda x:standardizeHeight(x))
print(len(heights))
print(heights)