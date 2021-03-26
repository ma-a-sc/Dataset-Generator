import numpy as np
import pandas as pd
import array_functions as af
import random


def create_variable(var_type, num_of_var):
    if var_type == "int":
        name = input("V_name")

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var) 

        ## still need to write a function that fills a defined array with 
        ## random integer. At the moment it is not in but float in a range of
        ## -2 to 2.
        int_array = pd.DataFrame(np.random.randn(how_many_var,1), index=indexes, 
        columns=(v_name))

        print(int_array)

    elif var_type == "float":
        name = input("V_name")

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var) 

        int_array = pd.DataFrame(np.random.randn(how_many_var,1), index=indexes, 
        columns=(v_name))

        print(int_array)


    elif var_type == "dummy":

        name = input("V_name")

        v_name =[name]

        how_many_var = num_of_var

        indexes = af.index_setter(how_many_var)



        int_array = pd.DataFrame(np.random.randn(how_many_var,1), index=indexes, columns=(v_name))

        print(int_array)

    elif var_type == "string":

        string_array = np.array([])

    elif var_type == "boolean":

        boolean_array = np.array([])

    else:
        exit()

def show_array():
    # print out the array
    pass

class descriptive_statistics():

    def __init__(self):
        pass

create_variable("int", 70)
