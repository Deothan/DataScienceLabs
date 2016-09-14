import csv
from Lab_2.Data import Data


class CSVReader:

    def __init__(self):
        self.list = []
        self.file = open("heights_raw.csv", newline="")
        self.reader = csv.reader(self.file)

    def readData( self ):
        for row in self.reader:
            self.list.append(Data(row[0], row[1], row[2]))

        return self.list
