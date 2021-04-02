from sys import exit
import numpy as np
import pandas as pd
import array_creating_functions as acf
from functools import reduce
import descriptive_statistics_functions as dsf

def user_inputs(): 
    how_many_vars = int(input("How many variables should be created?\n>"))

    which_type = input("""
What type of variable should be created?
int, float, dummy, string, boolean
>""")

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
    con = input("Do you want to add variables?\nyes/no\n>")

    if con == "yes":
        array = user_inputs()
        result = pd.concat(array, axis=1)
        list_of_results.append(result)

        recursive_user_input()

    elif con == "no":
        result_final = reduce(lambda left, right: pd.DataFrame.join(left, right), list_of_results)

        print(result_final)

        print(dsf.mean(result_final))
        
        exit()

    else:
        recursive_user_input()

def user_decisions():
    dec = input(print("""
Command Options:
generate dataset, load dataset, append dataset, variable options, exit
>"""))

    if dec == "generate dataset":
        recursive_user_input()

    elif dec == "load dataset":
        user_decisions()
        pass
    
    elif dec == "append dataset":
        user_decisions()
        pass
    elif dec == "variable options":
        user_decisions()
        pass
    elif dec == "exit":
        exit()
    else:
        print("Not a valid command. Try again.")
        user_decisions()


list_of_results = []


print("Hello, which of the following actions would you like to do?")
user_decisions()

