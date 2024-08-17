import random
f = open("616Char.csv","r")
dataIn = f.read()
list1 = dataIn.split("\n")

for i in range(10):
    n = random.randint(0,len(list1))
    print(list1[n])