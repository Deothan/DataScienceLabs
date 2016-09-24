import numpy as np
import pandas as pd

def convertToInches(tmp):
    if "'" in tmp:
        split = str.split(tmp,sep="'")
        print(split)
        return int(split[0])*12+int(split[1])
    if "." in tmp:
        split = str.split(tmp, sep=".")
        if "''" in split[1]:
            split[1][:-2]
        return int(split[0]) * 12 + int(split[1])

file2 = pd.read_csv("heights_raw.csv")
file2.columns = ['Time', 'Gender','Height']
file2 = file2.dropna()

print(file2)
file3 = file2.loc[(file2["Gender"]=="Female") & (file2["Gender"]== "Male")]
print(file3)

print(convertToInches("5.7"))