file = open("./lab4/task2.txt")

readed = file.read().replace("\n", " ")

print("з пробілами:",len(readed),"Без:",len(readed.replace(" ","")),sep='\n')


print("Кількість унікальних слів:",len(set(readed.split())))