import numpy as np
import pandas as pd
import random

## for float point numbers between 0 and 1
## random number in a range, int

## random list generator within a range

name = input("Name")

v_name = input("V_name")

vv_name =[v_name]

how_many_var = int(input("how many"))

randomlist = []
for i in range(0,how_many_var):
    q = random.randint(1,50)
    randomlist.append(q)

x = 0

indexes = []

we = 0

while x < how_many_var:
    indexes.append(we)
    x += 1
    we += 1

y = np.array(randomlist)

print(y)

s = pd.DataFrame(y(how_many_var,1), index=indexes, columns=(vv_name))

print(s)
