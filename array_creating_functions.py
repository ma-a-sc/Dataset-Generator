import numpy as np
import pandas as pd
import array_functions as af
import random


def create_variable(var_type, num_of_var):
    if var_type == "int":
        name = input("V_name")

        bot = int(input("Minimum"))

        top = int(input("Maximum"))

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var) 

        list_for_array = af.fill_int_aray(bot, top, num_of_var)
        
        int_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=(v_name))

        print(int_array)

    elif var_type == "float":
        name = input("V_name")

        bot = int(input("Minimum"))

        top = int(input("Maximum"))

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var) 

        list_for_array = af.fill_float_array(bot, top, num_of_var)

        float_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=(v_name))

        print(float_array)


    elif var_type == "dummy":

        name = input("V_name")

        bot = 0

        top = 1

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var) 

        list_for_array = af.fill_int_aray(bot, top, num_of_var)

        dummy_array = pd.DataFrame(list_for_array, index=indexes, 
        columns=(v_name))

        print(dummy_array)

    elif var_type == "string":
        name = input("V_name")

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var)

        ## A function is needed that fills the array randomly with the possibilities
        ## given by the user

        int_array = pd.DataFrame(np.random.randn(how_many_var,1), index=indexes, 
        columns=(v_name))

        print(int_array)

        string_array = np.array([])

    elif var_type == "boolean":
        name = input("V_name")

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var)

        ## Function mussing that fills the array with true and false. Is more or
        ## less the same as the dummy variable function.

        int_array = pd.DataFrame(np.random.randn(how_many_var,1), index=indexes, 
        columns=(v_name))

        print(int_array)

        boolean_array = np.array([])

    else:
        exit()

def show_array():
    # print out the array
    pass

class descriptive_statistics():

    def __init__(self):
        pass

create_variable("float", 70)
