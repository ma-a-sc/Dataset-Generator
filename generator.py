from sys import exit
import numpy as np
import pandas as pd
import array_creating_functions as acf
from functools import reduce

def user_inputs(): 
    how_many_vars = int(input("How many variables should be created?"))

    which_type = input("""
What type of variable should be created?
int, float, dummy, string, boolean
>
""")

    number_of_obs = int(input("How many observations should be created?\n>"))

    if which_type == "int":
        array = acf.array_creation_numbers(how_many_vars, which_type, number_of_obs)

    elif which_type == "float":
        array = acf.array_creation_numbers(how_many_vars, which_type, number_of_obs)

    elif which_type == "dummy":
        array = acf.array_creation_numbers(how_many_vars, which_type, number_of_obs)

    elif which_type == "string":
        array = acf.array_creation_string_bool(how_many_vars, which_type, number_of_obs)

    elif which_type == "boolean":
        array = acf.array_creation_string_bool(how_many_vars, which_type, number_of_obs)

    else:
        exit()

    return array


def recursive_user_input():
    con = input("Do you want to continue?\nyes/no\n>")

    if con == "yes":
        array = user_inputs()
        result = pd.concat(array, axis=1)
        list_of_results.append(result)

        recursive_user_input()

    elif con == "No":
        result_final = reduce(lambda left, right: pd.DataFrame.join(left, right), list_of_results)


        print(result_final)


        exit()

    else:
        recursive_user_input()

list_of_results = []

recursive_user_input()

