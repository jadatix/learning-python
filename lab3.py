from re import X


import csv
class Group:
    def __init__(self,num:int):
        self.num = num
        self.file = open(str(num)+".txt")
    def readFromFile(self):
        return csv.reader(self.file,delimiter="\n")
        
a = Group(414)
for i in a.readFromFile():
    print (a)
