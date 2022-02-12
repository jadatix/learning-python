import math
import random
import numpy as np
def game(target):
    flag = True;
    while flag:
        num=int(input("Введіть ваше число "))
        # flag = False if num==target else True
        if num==target:
            flag = False
            print("Ви вгадали ")
        elif num < target:
            print("ваше число менше" )
        else:
            print("ваше число більше ")
#Варіант 3

#task 1
# n=float(input("n= "))
# m=float(input("m= "))

# z=(math.sqrt(2)-math.sqrt(3*n))/(2*m)
# print(z)

#task2
a=random.randint(1,100)
game(a)

#task 3
# array=np.random.randint(-5,20,10)
# print(array)
# print(min(array))
# sum =0
# for i in range(len(array)):
#     if array[i]%2==0 and array[i]>0:
#         sum+=array[i]
# print(sum)

# for i in range(len(array)):
#     if array[i]>0:
#         print(array[i])



