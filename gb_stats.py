
# Importing required modules


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Helper functions to perform statistics


def pc5(x):
    # removing the nan values is necessary otherwise warning is given
    x_trim = x[~np.isnan(x)]
    return np.percentile(x_trim, 5)

def pc25(x):
    x_trim = x[~np.isnan(x)]
    return np.percentile(x_trim, 25)

def pc75(x):
    x_trim = x[~np.isnan(x)]
    return np.percentile(x_trim, 75)

def pc95(x):
    x_trim = x[~np.isnan(x)]
    return np.percentile(x_trim, 95)



def par_stats(par):
    
    '''
    input: numpy array or pandas Series 
    return: tuple of 11 elements
    
    Returns detailed descriptive statistics about the input data 
    - number of data points in the  set, mean, standard deviation, median, mean absolute deviation,
      minimum, 5th centila, 25th centile, 75th centile, 95th centile, maximum 
      of the time periods over the recording time 
    '''
    
    return (par.size, round(par.mean(), 4), round(par.std(), 4), round(par.median(), 4), round(par.mad(), 4),
            round(par.min(), 4), round(pc5(par.values), 4), round(pc25(par.values), 4),
            round(pc75(par.values), 4), round(pc95(par.values), 4), round(par.max(), 4))



def stats_calculator(obj, col):
    '''
    input: obj (Series or DataFrame), col (str)
    returns: tuple of size 8
    
    Calculates 8 different descriptive statistics for the data in the 'col' column of a series or dataframe
    '''
    
    a = obj[col]
    return (a.size, a.mean(), a.std(), a.median(), a.mad(), 
            a.min(), a.quantile(0.25), a.quantile(0.75), a.max())
