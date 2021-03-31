from sys import exit
import numpy as np
import pandas as pd
import array_creating_functions as acf


how_many_vars = int(input("How many variables should be created?"))

which_type = input("""
What type of variable should be created?
int, float, dummy, string, boolean
>
""")

number_of_obs = int(input("How many observations should be created?\n>"))

array = acf.array_creation_string_bool(how_many_vars, which_type, number_of_obs)

result = pd.concat(array, axis=1)

array2 = acf.array_creation_string_bool(how_many_vars, which_type, number_of_obs)

result2 = pd.concat(array2, axis=1)

array3 = pd.DataFrame.join(result, result2)


print(result)

print(result2)

print(array3)
