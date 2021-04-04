import numpy as np
import pandas as pd
import array_functions as af
import random


def create_variable_number(var_type, num_of_obs, bot, top):
    if var_type == "int":
        name = input("Variable name\n>")

        v_name =[name]

        how_many_obs = num_of_obs

        indexes = af.index_setter(how_many_obs) 

        list_for_array = af.fill_int_aray(bot, top, num_of_obs)
        
        int_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=v_name)

        return int_array

    elif var_type == "float":
        name = input("V_name")

        v_name =[name]

        how_many_obs = num_of_obs

        indexes = af.index_setter(how_many_obs) 

        list_for_array = af.fill_float_array(bot, top, num_of_obs)

        float_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=v_name)

        return float_array


    elif var_type == "dummy":

        name = input("V_name")

        no = 0

        yes = 1

        v_name =[name]

        how_many_obs = num_of_obs

        indexes = af.index_setter(how_many_obs) 

        list_for_array = af.fill_int_aray(no, yes, num_of_obs)

        dummy_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=v_name)
        
        return dummy_array

    else:
        exit()

        
def create_variable_string_boolean(var_type, num_of_obs):

    if var_type == "string":
        name = input("V_name")

        v_name =[name]

        how_many_obs = num_of_obs

        indexes = af.index_setter(how_many_obs)

        list_of_choices = af.choices_loop()

        list_for_array = af.fill_string_array(list_of_choices, num_of_obs)

        string_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=v_name)

        return string_array


    elif var_type == "boolean":
        name = input("V_name")

        v_name =[name]

        how_many_obs = num_of_obs

        indexes = af.index_setter(how_many_obs)

        list_of_choices = [True, False]

        array = af.fill_string_array(list_of_choices, num_of_obs)

        bool_array = pd.DataFrame(array, index=indexes, 
        columns=v_name)

        return bool_array

    else:
        exit()


def array_creation_numbers(how_many_vars, which_type, number_of_obs):
    x = 1

    bot = int(input("Minimum"))

    top = int(input("Maximum"))

    array = []

    while x <= how_many_vars:
        new_var = create_variable_number(which_type, number_of_obs, bot, top)
        array.append(new_var)
        x += 1

    return array

def array_creation_string_bool(how_many_vars, which_type, number_of_obs):
    x = 1
    array = []

    while x <= how_many_vars:
        new_var = create_variable_string_boolean(which_type, number_of_obs)
        array.append(new_var)
        x += 1

    return array

def store_dataframe(dataframe):
    dataframe.to_csv('out.csv')