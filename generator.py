from sys import exit
import numpy as np
import pandas as pd
from functools import reduce
import json

import array_creating_functions as acf
import descriptive_statistics_functions as dsf
import input_output_func as iof

### Within this programm I have often used the word array interchangeably with 
### list, arrays and dataframes. This is incorrect and I will fix this issue.
### However, at the moment the programm works as intended.


# The function reades the settings stored in the settings.txt file reads them
# and performs the operations based on the specified settings. It stores the 
# results in d_statistics_stored.

def descriptive_stats_ex(result_final):
    with open("settings.txt", 'r') as file:
        settings = file.read()
            
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


# The function asks the user for the number of variables, type of variable and 
# nuber of observations. Based on the type the array creating functions in
# array_creating_functions.py are called and the collected data
# is passed to the function. 
# In the end the results are return as array.

def user_inputs_for_array(): 
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

# The function first checks if the user wants to add more variables, because 
# the function calls it self.

def recursive_user_input():
    con = input("Do you want to add variables?\nyes/no\n>")

    # if the user specifies "yes" then the user_input_for_array function is called
    # and the result is then appended to the list_of_results.
    # Afterwards the function is called again for the chance that the user
    # wants to add more variables of the same or anohter type.
    if con == "yes":
        array = user_inputs_for_array()
        result = pd.concat(array, axis=1)
        list_of_results.append(result)

        recursive_user_input()

    # if the user specifies "no" then first the length of the list_of_results
    # is check in case the user has by accident typed in "no".
    # If the the list has results in it then the data in list_of_results
    # is merged from left to right unsing the indexes of the DataFrames to merge
    # on.
    elif con == "no":
        len_list_of_results = len(list_of_results)
        if len_list_of_results > 0:
        
            result_final = reduce(lambda left, right: pd.DataFrame.merge(left, right, left_index=True, right_index=True), list_of_results)

            print(result_final)

            # Here the length of the json object stored in settings.txt is checked
            # If there are options specified in it the length is >0. Then the
            # descripitce_stats_ex function is called with the completely merged
            # dataframe as argument.
            # Then the results of the descriptive statistics are also merged
            # based on their indexes.
            with open ("settings.txt", "r") as file:
                x = json.load(file)
                length_settings = len(x)
                if length_settings > 0:
                    d_statistics_stored = descriptive_stats_ex(result_final)

                    stats = reduce(lambda left, right: pd.DataFrame.merge(left, right, left_index=True, right_index=True), d_statistics_stored)

                    print(stats)

                else:
                    pass
            
            # The clearing of data is needed because the data in the list data
            # is passed to the function store_dataframe using the index of 0.
            # Data has to have only one entry to safe the DataFrame to either of 
            # file types.
            data.clear()
            data.append(result_final)
            user_decisions()
        else:
            print("\nNo data to merge.\n")
            recursive_user_input()

    else:
        recursive_user_input()

# This function takes the user input and stores it into a .txt file as a 
# json object. 

def descriptive_statistics_options():
    options = input("""
Which of the following options do you want to select?
Multiple can be selected using a semicolon
Options:
mean, median, min, max, mode, variance, standard deviation

>""")
    # replaces the spaces in the user input and splits the options
    # based on the semicolon in the input.
    options2 = options.replace(" ", "")
    options_split = options2.split(";")

    print(options)

    print(options_split)

    iof.new_json_txt(options_split, "settings.txt")

    user_decisions()


# safe_dataset safes the data stored in the list data at the index 0 to a file
# in the format specified by the user. At the end passes the information to 
# a storing function which has the logic to distinguish between the formats.

### Here the option for a path is missing. I should add that.

def safe_dataset():
    form = input("""
Which format should be used to safe the data?
Options:
csv, json, stata, excel

>""")

    name = input("""
Under what name should the dataset be safed?

>""")
    data2 = data[0]

    iof.store_dataframe(form, name, data2)
    user_decisions()

# load_dataset loads a dataset based on the user input and then asks to clear
# the information allready present in the programm (other generated or loaded
# data) or to append on it.

def load_dataset():
    form = input("""
What kind of dataset would you like to load?
Options:
csv, json, stata, excel

>""")

    name = input("""
What is the full name of the file?

>""")

    dataset = iof.load_dataframe(form, name)
    app_or_not = input("""
Do you want to append the allready loaded dataset or clear it first?
Options:
append, clear
>""")
    if app_or_not == "append":
        list_of_results.append(dataset)
    elif app_or_not == "clear":
        list_of_results.clear()
        list_of_results.append(dataset)
        data.clear()
    else:
        print("Invalid option specified")
        load_dataset()

    user_decisions()

# The function that is called at the end of all the functions within it.
# Used to determine what the user wants to do.

def user_decisions():
    dec = input("""
Command Options:
generate dataset, load dataset, safe dataset, append dataset, descriptive statistics options, clear all, exit

>""")

    if dec == "generate dataset":
        recursive_user_input()

    elif dec == "load dataset":
        load_dataset()

    elif dec == "safe dataset":
        safe_dataset()
    
    elif dec == "append dataset":
        recursive_user_input()

    elif dec == "descriptive statistics options":
        descriptive_statistics_options()

    elif dec == "clear all":
        iof.clear_txt("settings.txt")
        list_of_results.clear()
        data.clear()
        user_decisions()

    elif dec == "exit":

        exit()
    else:
        print("Not a valid command. Try again.\n\n")
        user_decisions()

list_of_results = []

data = []

print("Hello, which of the following actions would you like to do?")
user_decisions()
