import numpy as np

def create_variable(var_type, num_of_var):
    if var_type == "int":
        int_array_empty = np.zeros((1, num_of_var))
        print(int_array_empty)
        int_array = np.array([])

    elif var_type == "float":

        float_array = np.array([])

    elif var_type == "dummy":

        dummy_array = np.array([])

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


### the code that i need to fuse 1d arrays into 2ds and with the 1ds stacked

a = np.array([4.,2.])
>>> b = np.array([3.,8.])
>>> np.column_stack((a,b))     # returns a 2D array
array([[4., 3.],
       [2., 8.]])