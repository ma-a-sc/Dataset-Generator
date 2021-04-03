from sys import exit
import numpy as np
import pandas as pd
from functools import reduce
import json

import array_creating_functions as acf
import descriptive_statistics_functions as dsf
import input_output_func as iof


def descriptive_stats_ex(result_final):
    with open("settings.txt", 'r') as m:
        settings = m.read()
            
    settings_var = json.loads(settings)
    print(settings_var)

    d_statistics_stored = []

    for i in settings_var:
        if i == "mean":
            var_mean = dsf.mean(result_final)
            var_mean_frame = pd.DataFrame(var_mean)
            d_statistics_stored.append(var_mean_frame)

        elif i == "median":
            var_median = dsf.median(result_final)
            var_median_frame = pd.DataFrame(var_median)
            d_statistics_stored.append(var_median_frame)
            
        elif i == "min":
            var_min = dsf.v_min(result_final)
            var_min_frame = pd.DataFrame(var_min)
            d_statistics_stored.append(var_min_frame)

        elif i == "max":
            var_max = dsf.v_max(result_final)
            var_max_frame = pd.DataFrame(var_max)
            d_statistics_stored.append(var_max_frame)

        elif i == "mode":
            var_mode = dsf.mode(result_final)
            var_mode_frame = pd.DataFrame(var_mode)
            d_statistics_stored.append(var_mode_frame)
            
        elif i == "variance":
            var_variance = dsf.variance(result_final)
            var_variance_frame = pd.DataFrame(var_variance)
            d_statistics_stored.append(var_variance_frame)
            
        elif i == "standard deviation":
            var_standard_deviation = dsf.standard_deviation(result_final)
            var_standard_deviation_frame = pd.DataFrame(var_standard_deviation)
            d_statistics_stored.append(var_standard_deviation_frame)

        else:
            print("Invalid options specified. Try again.")
            d_statistics_stored.clear()

            g.user_decisions()

    print(d_statistics_stored)

    return d_statistics_stored

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

        d_statistics_stored = descriptive_stats_ex(result_final)

        stats = reduce(lambda left, right: pd.DataFrame.join(left, right), d_statistics_stored)

        print(stats)

        exit()

    else:
        recursive_user_input()


def descriptive_statistics():
    options = input("""
Which of the following options do you want to select?
Multiple can be selected using a semicolon
Options:
mean, median, min, max, mode, variance, standard deviation
>""")

    options2 = options.replace(" ", "")
    options_split = options2.split(";")

    print(options)

    print(options_split)

    iof.new_json_txt(options_split)

    user_decisions()


def user_decisions():
    dec = input("""
Command Options:
generate dataset, load dataset, append dataset, descriptive statistics, exit
>""")

    if dec == "generate dataset":
        recursive_user_input()

    elif dec == "load dataset":
        pass
    
    elif dec == "append dataset":
        pass
    elif dec == "descriptive statistics":
        descriptive_statistics()

    elif dec == "exit":

        iof.clear_txt("settings.txt")

        exit()
    else:
        print("Not a valid command. Try again.\n\n")
        user_decisions()


list_of_results = []


print("Hello, which of the following actions would you like to do?")
user_decisions()

