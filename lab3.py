import sys
import csv
from tokenize import group
class Group:
    def __init__(self,num:int):
        self.num = num
        self.file =str(num)+".txt"
        
    def read(self):
        with open(self.file) as file:
            lines = [line.rstrip() for line in file]
            return lines

    def write(self, lines:list):
        with open(self.file,"w") as file:
           file.writelines([line+'\n' for line in lines])
    
    def append(self, lines:list):
        with open(self.file, "a") as file:
           file.writelines([line+'\n' for line in lines])
           
    def find_ny_name(self,name:str):
        return [line for line in self.read() if name in line]
    
    def sort(self):
        self.write(sorted(self.read(),
            key=lambda line: int(line.split()[1])))
        return self
        

    
        
group = int(input("Enter a group "))
a = Group(group)
print(a.read())
print(a.find_ny_name("Андрій"))
print("sorted",a.sort().read(),sep='\n')
