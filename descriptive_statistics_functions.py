import pandas as pd

def mean(array):
    result = array.mean(axis=0)
    print("\nMean")
    print(result)

    return result

def median(array):
    result = array.mean(axis=0)
    print("\nMedian")
    print(result)
    return result

def v_min(array):
    result = array.min(axis=0)
    print("\nMin")
    print(result)
    return result
    
def v_max(array):
    result = array.max(axis=0)
    print("\nMax")
    print(result)
    return result
    
def mode(array):
    result = array.mode(axis=0)
    print("\nMode")
    print(result)
    return result

def variance(array):
    result = array.var(axis=0)
    print("\nVariance")
    print(result)
    return result

def standard_deviation(array):
    result = array.std(axis=0)
    print("\nStandard Deviation")
    print(result)
    return result


