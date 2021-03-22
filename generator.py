from sys import exit
import numpy as np
import array_creating_functions


def new_array():

    var_type = input("""What type of variable would you like the variables to be?
    >""")

    num_of_variables = input(f"""
    How many of these {var_type} variables should be generated?"""
    )

    array_creating_functions.create_variable(var_type, num_of_variables)

    new_array()
    



print("pass")