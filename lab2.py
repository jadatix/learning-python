from numpy import sort
from qsort import quickSort

def listWithOutDublicates(inList):
    return list(set(inList))

def findByVal(inList: list, value):
    return inList.index(value)

def findSeq(inList: list, sequence:list):
    for i in range(len(inList)-len(sequence)):
        if(inList[i:i+len(sequence)] == sequence):
            return [i,i+len(sequence)-1]

def firstMin5(inList: list,minFlag = True):   
    if minFlag:
        return sorted(inList)[:5]
    else:
        return sorted(inList)[-5:]

def average(inList: list):
    return sum(inList)/len(inList)


a=[1,2,3,1,3,2,13,2,1]
b=[2,13,2]
print(a)
print(b)

# print(listWithOutDublicates(a))
# quickSort(a,0,len(a)-1)
# findSeq(a,b)
# print(firstMin5(a))
print(average(a))


