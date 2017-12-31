import random
import math
list = [1,1]
randnum = random.random()
currentnum = math.ceil(randnum) * 2
while currentnum >= len(list):
    list.append(list[(currentnum-2)] + list[(currentnum-1)])
    currentnum = currentnum + 1
    tempnum = currentnum - 3
    print(list[tempnum])