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
    print(f"\n\n{settings_var}")

    d_statistics_stored = []

    for i in settings_var:
        if i == "mean":
            x = ["Mean"]
            var_mean = dsf.mean(result_final)
            var_mean_frame = pd.DataFrame(var_mean, columns=x)
            d_statistics_stored.append(var_mean_frame)

        elif i == "median":
            x = ["Median"]
            var_median = dsf.median(result_final)
            var_median_frame = pd.DataFrame(var_median, columns=x)
            d_statistics_stored.append(var_median_frame)
            
        elif i == "min":
            x = ["Min"]
            var_min = dsf.v_min(result_final)
            var_min_frame = pd.DataFrame(var_min, columns=x)
            d_statistics_stored.append(var_min_frame)

        elif i == "max":
            x = ["Max"]
            var_max = dsf.v_max(result_final)
            var_max_frame = pd.DataFrame(var_max, columns=x)
            d_statistics_stored.append(var_max_frame)

        elif i == "mode":
            x = ["Mode"]
            var_mode = dsf.mode(result_final)
            var_mode_frame = pd.DataFrame(var_mode, columns=x)
            d_statistics_stored.append(var_mode_frame)
            
        elif i == "variance":
            x = ["Variance"]
            var_variance = dsf.variance(result_final)
            var_variance_frame = pd.DataFrame(var_variance, columns=x)
            d_statistics_stored.append(var_variance_frame)
            
        elif i == "standard deviation":
            x = ["Standard Deviation"]
            var_standard_deviation = dsf.standard_deviation(result_final)
            var_standard_deviation_frame = pd.DataFrame(var_standard_deviation, columns=x)
            d_statistics_stored.append(var_standard_deviation_frame)

        else:
            print("Invalid options specified. Try again.")
            d_statistics_stored.clear()

            user_decisions()


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

        acf.store_dataframe(result_final)

        d_statistics_stored = descriptive_stats_ex(result_final)

        ## here I have to re write it. Either find a way to use the var names as indexes to join on
        ## or to user .merge instead. But I dont know how that works with lambda.
        stats = reduce(lambda left, right: pd.DataFrame.merge(left, right, left_index=True, right_index=True), d_statistics_stored)

        print(stats)

        user_decisions()

    else:
        recursive_user_input()


def descriptive_statistics_options():
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
generate dataset, load dataset, safe dataset, append dataset, descriptive statistics options, exit
>""")

    if dec == "generate dataset":
        recursive_user_input()

    elif dec == "load dataset":
        load_dataset()
        pass

    elif dec == "safe dataset":
        safe_dataset()
        pass
    elif dec == "append dataset":
        pass
    elif dec == "descriptive statistics options":
        descriptive_statistics_options()

    elif dec == "exit":

        iof.clear_txt("settings.txt")

        exit()
    else:
        print("Not a valid command. Try again.\n\n")
        user_decisions()

list_of_results = []

print("Hello, which of the following actions would you like to do?")
user_decisions()

