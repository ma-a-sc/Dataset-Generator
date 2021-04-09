import pandas as pd

### This whole file is only used to return the mean, median etc of the 
### array passed to the respective functions.
### axis=0 is used to get the column names to index side of the final output of 
### the function that calls these functions. The column name will be the 
### respective descriptive option defined by the user.

def mean(array):
    
    result = array.mean(axis=0)
    return result

def median(array):
    
    result = array.mean(axis=0)
    return result

def v_min(array):
    
    result = array.min(axis=0)
    return result
    
def v_max(array):
    
    result = array.max(axis=0)
    return result
    
def mode(array):
    
    result = array.mode(axis=0)
    return result

def variance(array):
    
    result = array.var(axis=0)
    return result

def standard_deviation(array):
    
    result = array.std(axis=0)
    return result


