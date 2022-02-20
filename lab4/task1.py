from random import randint
import numpy as np

files = [open("./lab4/"+str(i+1)+".txt") for i in range(3)]
res =""
for file in files:
    readed= file.read().split()
    res+=readed[randint(0, len(readed)-1)]+ " "

print(res)
