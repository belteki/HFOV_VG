
# Importing required modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Functions to load ventilator data


def data_loader(lst):
    
    '''
    list ->  DataFrame 
    
    - Takes a list of csv files (given as filenames with absolute paths) and import them as a dataframes 
    - Combines the 'Date' and 'Time' columns into a Datetime index while keeping the original columns
    - If there are more files it concatenates them into a single dataframe. 
    - It returns the concatenated data as one DataFrame. 
    
    '''
    data  = []
    for i, filename in enumerate(lst):
        data.append(pd.read_csv(lst[i], keep_date_col = 'True', parse_dates = [['Date', 'Time']])) 
    data = pd.concat(data) 
    data.index = data.Date_Time
    return data


# "fast_Unknown" files contain the parameters (pressure, flow, volume) obtained at 100Hz (100/sec) sampling rate
def fast_data_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_fast_Unknown.csv'
    '''
    return [n for n in lst if n.endswith('_fast_Unknown.csv')]


# "slow_Text" files contain the the ventilator modes, basic ventilator settings, etCO2 data if available
def slow_text_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_slow_Text.csv'
    '''
    return [n for n in lst if n.endswith('_slow_Text.csv')]


# "slow_Setting" files contain the the ventilator settings and their changes
def slow_setting_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_slow_Setting.csv'
    '''
    return [n for n in lst if n.endswith('_slow_Setting.csv')]



# "slow_Measurements" are all the ventilator parameters obtained at 1Hz (1/sec) sampling rate
def slow_measurement_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with 'Measurement.csv''
    '''
    return [n for n in lst if n.endswith('_slow_Measurement.csv')]


# "slow_Measurements" are all the ventilator parameters obtained at 1Hz (1/sec) sampling rate
def alarm_setting_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_slow_AlarmSetting.csv'
    '''
    return [n for n in lst if n.endswith('_slow_AlarmSetting.csv')]


# "slow_AlarmState" are all the alarm events obtained with a microsecond time stamp
def alarm_state_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_slow_AlarmState.csv'
    '''
    return [n for n in lst if n.endswith('_slow_AlarmState.csv')]


# "annotations" are textual annotations entered by the user. They have a microsecond timestamp.
def annotation_finder(lst):
    '''
    list -> list
    
    Takes a list of filenames and returns those ones that end with '_annotations.csv'
    '''
    return [n for n in lst if n.endswith('_annotations.csv')]


## Functions to load blood gases


def blood_gas_loader(path, dct, recording):
    '''
    str, dict, str -> None
    
    - path: filename with path of excel file containing the blood gases
    - dct: dictionary to contain blood gases;
    - recording: recording name

    Import blood gases as DataFrames into the dictionary 'dct'. This function modifies dct dictionary
    in place and return 'None'.

    '''
    dct[recording] = pd.read_excel(path, sheetname = recording[:5], header = None)
    dct[recording] = pd.DataFrame(dct[recording].T)
    dct[recording].columns = dct[recording].iloc[0]
    dct[recording] = dct[recording][1:]
    dct[recording].index = [dct[recording]['Date:'], dct[recording]['Time:']]




