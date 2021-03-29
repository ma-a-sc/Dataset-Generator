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

if which_type == "int":
    array = acf.array_creation_numbers
    (how_many_vars, which_type, number_of_obs)

elif which_type == "float":
    array = acf.array_creation_numbers
    (how_many_vars, which_type, number_of_obs)

elif which_type == "dummy":
    array = acf.array_creation_numbers
    (how_many_vars, which_type, number_of_obs)

elif which_type == "string":
    array = acf.array_creation_string_bool2
    (how_many_vars, which_type, number_of_obs)


elif which_type == "boolean":
    array = acf.array_creation_string_bool
    (how_many_vars, which_type, number_of_obs)

else:
    exit()

result = pd.concat(array, axis=1)
print(result)
