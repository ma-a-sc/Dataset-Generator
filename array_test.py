import numpy as np
import random

## for float point numbers between 0 and 1
## random number in a range, int

## random list generator within a range
randomlist = []
for i in range(0,5):
    q = random.randint(1,50)
    randomlist.append(q)

print(randomlist)

name = input("Name")

x = np.array([(name, randomlist)])

print(x)