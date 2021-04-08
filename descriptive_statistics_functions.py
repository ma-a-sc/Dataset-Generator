import pandas as pd

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


