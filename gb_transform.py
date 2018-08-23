
# Importing required modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### Functions to preprocess ventilator settings, modes and alarm settings

def vent_mode_cleaner(inp):
    '''
    DataFrame -> DataFrame

    Takes a DataFrame of ventilator modes ('slow_text')
    and removes the unimmportant parameters and changes
    '''
    a = inp[inp.Id != 'Device is in neonatal mode']
    a = a[a.Id != 'Device is in neonatal mode']
    a = a[a.Id != 'Selected CO2 unit is mmHg']
    a = a[a.Id != "Selected language (variable text string transmitted with this code, see 'MEDIBUS.X, Rules and Standards for Implementation' for further information)"]
    a = a[a.Id != 'Device configured for intubated patient ventilation']
    a = a[a.Id != 'Active humid heated']
    a = a[a.Id != 'Audio pause active']
    a = a[a.Id != 'Active humid unheated']
    a = a[a.Id != 'Suction maneuver active']
    a.drop_duplicates(["Rel.Time [s]", "Id"], inplace = True)
    return a


def vent_settings_cleaner(inp):
    '''
    DataFrame -> DataFrame

    Takes a DataFrame of ventilator settings ('slow_settings')
    and removes the unimmportant parameters and changes
    '''
    a = inp[inp.Id != 'FiO2']
    a = a[a.Id != 'Ø tube']
    a = a[a.Id != 'Tapn']
    a = a[a.Id != 'ΔPsupp']
    a = a[a.Id != 'Tube Æ']
    a = a[a.Id != 'RRsigh']
    a = a[a.Id != 'Psigh']
    a = a[a.Id != 'Slopesigh']
    a = a[a.Unit != 'L']
    a = a[a.Id != 'I (I:E)']
    a = a[a.Id != 'E (I:E)']
    a = a[a.Id != 'MVlow delay']
    a = a[a.Id != 'MVhigh delay']
    a.drop_duplicates(["Rel.Time [s]", "Name"], inplace = True)
    return a


def alarm_setting_cleaner(dframe):
    '''
    DataFrame -> DataFrame

    Takes a DataFrame of alarm settings ('alarm_settings')
    and removes the unimmportant etCO2 alarms as etCO2 was not used
    ''' 
    a = dframe[dframe.Id != 'etCO2_LL']
    a = a[a.Id != 'etCO2_HL']
    a.drop_duplicates(['Rel.Time [s]', 'Name'], inplace = True)
    return a



### Functions to preprocess fast data

def fast_data_processor(fast_data):
    '''
    DataFrame -> DataFrame
    Removes duplicated time stamps by shifting the time for the duplications
    by 8 mssec
    '''
    fast_data = fast_data[[ 'Date_Time', 'Rel.Time [s]', '5001|Paw [mbar]', 
                       '5001|Flow [L/min]', '5001|Volume [mL]']]
    fast_data.columns = ['date_time', 'rel_time_s', 'paw', 'flow', 'volume']
    fast_data['row_num'] = np.arange(len(fast_data))

    # Remove duplicated time stamps (this will take a couple minutes)
    
    mask = fast_data.duplicated(subset = 'date_time')
    uniq = fast_data[~mask]
    dupl = fast_data[mask]
    uniq.index = uniq.ix[:].date_time
    dupl.index = dupl.ix[:].date_time.apply(lambda x: x + pd.offsets.Milli(8))
    fast_data_non_dupl = pd.concat([uniq, dupl])
    fast_data_non_dupl = fast_data_non_dupl.sort_index()
    fast_data_non_dupl = fast_data_non_dupl.drop('date_time', axis = 1)
    fast_data = fast_data_non_dupl
    
    fast_data.replace(to_replace = {'flow': {0.045: 0}}, inplace = True)
    fast_data.replace(to_replace = {'flow': {-0.045: 0}}, inplace = True)
    
    return fast_data

