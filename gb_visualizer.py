
# Importing required modules

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



### Function to visualise  slow ventilation data

par_list = {} # library parameter lists
ytitle = {} # library of y axis titles for various parameter lists


par_list['FiO2'] = ('FiO2',) # to create a one-element tuple, comma needs to be added at the end

par_list['PIP'] = ('PIP',)
par_list['MAP'] = ('Pmean',)
par_list['pressures'] = ('PIP', 'Pmean', 'PEEP' )
par_list['high_pressures'] = ('PIP', 'EIP')
par_list['low_pressures'] = ('Pmin', 'PEEP')

par_list['VT'] = ('VT_kg',)
par_list['VTs'] = ('VTi_kg', 'VT_kg', 'VTe_kg')
par_list['VTmand'] = ('VTmand_kg',)
par_list['VTspon'] = ('VTspon_kg',)
par_list['VTmandspon'] = ('VTmand_kg', 'VTspon_kg')
par_list['VTmands'] = ('VTimand_kg','VTmand_kg', 'VTemand_kg')
par_list['VTspons'] = ('VTispon_kg', 'VTspon_kg', 'VTespon_kg')
par_list['VTis'] =  ('VTimand_kg', 'VTispon_kg')
par_list['VTes'] = ('VTemand_kg', 'VTespon_kg')

par_list['MV'] = ('MV_kg',)
par_list['MVs'] = ('MVi_kg', 'MV_kg', 'MVe_kg')
par_list['MVmandspon'] = ('MVemand_kg', 'MVespon_kg')
par_list['MVspon%'] = ('MVspon%',)

par_list['MVleak'] = ('MVleak_kg',)
par_list['leak%'] = ('leak%',)

par_list['RR'] = ('RR',)
par_list['RRs'] = ('RR', 'RRmand', 'RRspon')

par_list['flow'] = ('FlowDev',)
par_list['Tispon'] = ('Tispon',)
par_list['E_time'] = ('E_IE',)

par_list['C'] = ('Cdyn',)
par_list['Cs'] = ('Cdyn', 'C20_Cdyn')
par_list['R'] = ('R',)
par_list['TC'] = ('TC',)
par_list['TCs'] = ('TC', 'TCe')
par_list['r2'] = ('r2',)

par_list['Phf'] = ('amplitude',)
par_list['VThf'] = ('VThf_kg',)
par_list['DCO2'] = ('DCO2',)
par_list['DCO2_corr'] = ('DCO2_corr_kg',)



ytitle[('FiO2',)] = 'FiO2 (%)'

ytitle[('PIP',)] = 'Pressure (mBar)'
ytitle[('Pmean',)] = 'Pressure (mBar)'
ytitle[('PIP', 'Pmean', 'PEEP' )] = 'Pressure (mBar)'
ytitle[('PIP', 'EIP')] = 'Pressure (mBar)'
ytitle[('Pmin', 'PEEP')] = 'Pressure (mBar)'

ytitle[('VT_kg',)] = 'Tidal volume (mL/kg)'
ytitle[('VTi_kg', 'VT_kg', 'VTe_kg')] = 'Tidal volume (mL/kg)'
ytitle[('VTmand_kg', )] = 'Tidal volume (mL/kg)'
ytitle[('VTspon_kg', )] = 'Tidal volume (mL/kg)'
ytitle[('VTmand_kg', 'VTspon_kg')] = 'Tidal volume (mL/kg)'
ytitle[('VTimand_kg','VTmand_kg', 'VTemand_kg')] = 'Tidal volume (mL/kg)'
ytitle[('VTispon_kg', 'VTspon_kg', 'VTespon_kg')] = 'Tidal volume (mL/kg)'
ytitle[('VTimand_kg', 'VTispon_kg')] = 'Tidal volume (mL/kg)'
ytitle[('VTemand_kg', 'VTespon_kg')] = 'Tidal volume (mL/kg)'

ytitle[('MV_kg',)] = 'Minute volume (mL/kg/min)'
ytitle[('MVi_kg', 'MV_kg', 'MVe_kg')] = 'Minute volume (mL/kg/min)'
ytitle[('MVemand_kg', 'MVespon_kg')] = 'Minute volume (mL/kg/min)'
ytitle[('MVspon%',)] = '%'

ytitle[('MVleak',)] = ('Minute volume (mL/kg/min)')
ytitle[('leak%',)] = ('Leak (%)')

ytitle[('RR',)] = 'Respiratory rate (1/min)'
ytitle[('RR', 'RRmand', 'RRspon')] = 'Respiratory rate (1/min)'

ytitle[('flow',)] = 'Flow (L/min)'
ytitle[('Tispon',)] = 'Time (sec)'
ytitle[('E_IE', )] = 'Expiratory time / Inspiratory time (ratio)'

ytitle[('Cdyn', )] = 'Compliance (L/Bar)'
ytitle[('Cdyn', 'C20_Cdyn')] = 'Compliance (L/Bar)'
ytitle[('R',)] = 'Resistance (mBar/L/sec)'
ytitle[('TC', )] = 'Time constant (sec)'
ytitle[('TC', 'TCe')] = 'Time constant (sec)'
ytitle[('r2',)] = 'Unit'

ytitle[('amplitude',)] = 'Ampliture pressure (mBar)'
ytitle[('VThf_kg',)] = 'High frequency tidal volume (mL/kg)'
ytitle[('DCO2',)] = 'DCO2 (10 * mL2/sec)'
ytitle[('DCO2_corr_kg',)] = 'weight-corrected DCO2 (mL2/kg2/sec)'



def plot_data_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  1/sec data' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);



def plot_data_mean_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements_1min_mean[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements_1min_mean[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  1-min means' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s_1min_mean.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);


def plot_data_median_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements_1min_med[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements_1min_med[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  1-min medians' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s_1min_med.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);



def plot_data_sd_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements_1min_std[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements_1min_std[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  1-min standard deviations' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s_1min_sd.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);





def plot_data_iqr_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements_1min_iqr[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements_1min_iqr[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  1-min interquartile ranges' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s_1min_iqr.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);





def plot_data_rw_file(rec, parameters, lim = False, col = False, filetype = 'jpg', dpi = 300):
    
    '''
    Input:
    - rec: recording name (str)
    - parameters: key of the par_list dictionary (str)
    - lim: high limit of the y axis (float)
    - col: list of colors to be used in the plot on consecutive graphs (strings)
    - filetype: the image file type (str)
    - dpi: resolution in dot per inch (int)
    Returns: None
    
    Export a plot using the data of recording REC, visualising the parameters of par_list[PARAMETERS]
    using y-axis high limit LIM if given, otherwise the high limit will be 1.2 times the highest of the maximums 
    of the visualised parameters. Uses colours of COL, other uses ['red', 'green', 'blue', 'black'] 
    The filetype will be FYLETYPE or .jpg if not given. The resolution will be DPI dot per inch or 100 if not given.
    
    '''
    pl = par_list[parameters]
    ax = list(range(len(pl)))
    
    try:
        y = ytitle[pl]
    except KeyError:
        y = ''

    if not lim:
        limit = []
        for i in range(len(pl)):
            limit.append(slow_measurements_3h_rw[rec][pl[i]].max())                                                                 
        limit = max(limit)
        limits = [0, limit * 1.2]
    else:
        limits = lim
    
    if not col:
        color = ['red', 'blue', 'green', 'black']
    else:
        color = col  
    
    fig = plt.figure()
    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=None, bottom=0.2, right=None, top=None, wspace=None, hspace=None)
    ax[0] = fig.add_subplot(1, 1, 1)

    for i, par in enumerate(pl):
        slow_measurements_3h_rw[rec][pl[i]].plot(ax = ax[0], color = color[i], ylim = limits)
                                                          
    ax[0].set_xlabel('Time (hours)', size = 12, color = 'black')
    ax[0].set_ylabel(y, size = 12, color = 'black')
    ax[0].set_title('%s -  3-hours rolling windows' % rec,  size = 12, color = 'black')
    ax[0].legend(pl, fontsize = 12)

    ax[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax[0].tick_params(which = 'both', labelsize=12)

    fig.savefig('%s/%s/%s_%s_3h_rw.%s' % (DATA_DUMP, rec, rec, parameters, filetype),
            dpi = dpi, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format = filetype,
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True);







### Visualising fast data

def waves_drawer(fast, i, wr):
    '''
    
    Argument (i): an element of pandas DatetimeIndex object (not the last one)
    returns: None
    
    Prints pressure, flow and volume curves between i and the next DatetimeIndex as graph
    
    '''
    
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex = 'all', sharey = 'none')
    fig.set_size_inches(15,15); fig.set_label('res')
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.1)
    
    fast.loc[i : i+1].paw.plot(ax = axes[0], color = 'red', title = 'Pressure', 
            linewidth=2, ylim = [0, (fast.loc[i : i+1].paw.max() * 1.2)])
    fast.loc[i : i+1].flow.plot(ax = axes[1], color = 'green', title = 'Flow', 
            linewidth=2, ylim = [(fast.loc[i : i+1].flow.min() * 1.2), 
                                 (fast.loc[i : i+1].flow.max() * 1.2)]);
    xmin, xmax = axes[1].get_xlim()
    axes[1].hlines(0, xmin, xmax, color = 'black', linewidth = 2)

    fast.loc[i : i+1].volume.plot(ax = axes[2], color = 'blue', title = 'Volume', 
            linewidth=2, rot= 0, ylim = [0, (fast.loc[i : i+1].volume.max() * 1.2)])
    
    axes[0].set_xlabel(''); axes[1].set_xlabel(''); axes[2].set_xlabel('Time', size = 22, 
            color = 'black', rotation = 0 )
    axes[0].set_ylabel('mbar', size = 14, color = 'black')
    axes[1].set_ylabel('L/min', size = 14, color = 'black')
    axes[2].set_ylabel('mL', size = 14, color = 'black')

    axes[0].set_title('Pressure', size = 16, color = 'black')
    axes[1].set_title('Flow', size = 16, color = 'black')
    axes[2].set_title('Volume', size = 16, color = 'black')

    axes[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray') 
    axes[1].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    axes[2].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    
    axes[2].set_xlabel('Time')

    if wr:
        fig.savefig('%s/%s_waves_long_%s.%s' % (dir_write, recording, i, 'jpg'), 
            dpi = 200, facecolor='w', edgecolor='w', orientation='portrait', 
            papertype=None, format = 'jpg', transparent=False, bbox_inches=None, 
            pad_inches=0.1, frameon=True)



def waves_long(fast_data, start , end, write = False):
    '''
    Arguments: start (string), end (string)
    Returns None
    
    Creates a DatetimeIndex object between 'start' and 'end' with a 
    period of 1 min between the elements.
    Calls the waves_drawer function on the elements of this DatetimeIndex list 
    (except the last element)
    
    Example:waves('2016-06-25 06:00:00', '2016-06-25 06:02:00') creates the list:
    DatetimeIndex(['2016-06-25 06:00:00', '2016-06-25 06:01:00', '2016-06-25 06:02:00'],
              dtype='datetime64[ns]', freq='T')
   
   '''
    timelist = pd.date_range(start, end, freq = '1min')
    for i in timelist[:-1]:
        waves_drawer(fast_data, i, write)





def waves_short(fast_data, start , end,  j = 1, write = False):
    fig, axes = plt.subplots(nrows=3, ncols=1)
    fig.set_size_inches(15,15); fig.set_label('res')

    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.15, hspace=0.3)
    
    fast_data.loc[start : end].paw.plot(ax = axes[0], color = 'red', title = 'Pressure', 
            linewidth=1, ylim = [0, (fast_data.loc[start : end].paw.max() * 1.2)])
    fast_data.loc[start : end].flow.plot(ax = axes[1], color = 'green', title = 'Flow', 
            linewidth=1, ylim = [(fast_data.loc[start : end].flow.min() * 1.2), 
                                 (fast_data.loc[start : end].flow.max() * 1.2)])
    xmin, xmax = axes[1].get_xlim()
    axes[1].hlines(0, xmin, xmax, color = 'black', linewidth = 1)
    fast_data.loc[start : end].volume.plot(ax = axes[2], color = 'blue', title = 'Volume', 
            linewidth=1, rot= 0, ylim = [0, (fast_data.loc[start : end].volume.max() * 1.2)])

    axes[0].set_xlabel(''); axes[1].set_xlabel(''); axes[2].set_xlabel('Time', size = 12, 
            color = 'black', rotation = 0 )
    axes[0].set_ylabel('mBar', size = 12, color = 'black')
    axes[1].set_ylabel('L/min', size = 12, color = 'black')
    axes[2].set_ylabel('mL', size = 12, color = 'black')

    for i in range(2):
        axes[i].get_xaxis().set_visible(False)
        axes[i].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    
    if write:
        fig.savefig('%s/%s_waves_short_%s.%s' % (dir_write, recording, j, 'jpg'), dpi = 200, facecolor='w',
            edgecolor='w', orientation='portrait', papertype=None, format = 'jpg',
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True)



def wave_individual(br, j = 1,  write = False):
    fig, axes = plt.subplots(nrows=3, ncols=1, sharex = 'all', sharey = 'none')
    fig.set_size_inches(15,12); fig.set_label('res')
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.15)
    
    br.paw.plot(ax = axes[0], color = 'red', title = 'Pressure', linewidth=2, 
                ylim = [0, (br.paw.max() * 1.2)]);
    br.flow.plot(ax = axes[1], color = 'green', title = 'Flow', linewidth=2,
                ylim = [(br.flow.min() * 1.2), (br.flow.max() * 1.2)])
    xmin, xmax = axes[1].get_xlim()
    axes[1].hlines(0, xmin, xmax, color = 'black', linewidth = 2)
    br.vol_from_flow.plot(ax = axes[2], color = 'blue', title = 'Volume', linewidth=2, 
                ylim = [-0.1, (br.vol_from_flow.max() * 1.2)])
    
    axes[0].set_xlabel(''); axes[1].set_xlabel('')
    axes[2].set_xlabel('Time', size = 20, color = 'black', rotation = 0 )
    axes[0].set_ylabel('mbar', size = 20, color = 'black')
    axes[1].set_ylabel('L/min', size = 20, color = 'black')
    axes[2].set_ylabel('mL', size = 20, color = 'black')
    axes[0].set_title('Pressure', size = 20, color = 'black')
    axes[1].set_title('Flow', size = 20, color = 'black')
    axes[2].set_title('Volume', size = 20, color = 'black')

    axes[0].grid('on', linestyle='-', linewidth=0.5, color = 'gray') 
    axes[1].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    axes[2].grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    
    if write:
        fig.savefig('%s/%s_wave_individual_%s.%s' % (dir_write, recording, j, 'jpg'), dpi = 200, facecolor='w',
            edgecolor='w', orientation='portrait', papertype=None, format = 'jpg',
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True)


def loop(br, j = 1, write = False):
    fig, (ax0, ax1) = plt.subplots(1, 2)
    fig.set_size_inches(12,6)
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.2)
    
    x = br.paw
    y = br.flow
    z = br.vol_from_flow

    ax0.plot(x, z, linewidth = 2, color = 'red')
    ax0.set(xlim = [0, (x.max() * 1.2)], ylim = [0, (z.max() * 1.2)])

    ax0.set_title('Pressure - Volume loop', size = 20, color = 'black')
    ax0.set_xlabel('Pressure (mBar)', size = 16, color = 'black')
    ax0.set_ylabel('Volume (mL)', size = 16, color = 'black')
    ax0.grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax0.legend().set_visible(False)
  
    ax1.plot(y, z, linewidth = 2, color = 'blue')
    ax1.set(xlim = [y.min() * 1.2, (y.max() * 1.2)], ylim = [0, (z.max() * 1.2)])
    
    ax1.set_title('Flow - Volume loop', size = 20, color = 'black')
    ax1.set_xlabel('Flow (L/min)', size = 16, color = 'black')
    ax1.set_ylabel('Volume (mL)', size = 16, color = 'black')
    ax1.grid('on', linestyle='-', linewidth=0.5, color = 'gray')
    ax1.legend().set_visible(False)
    
    if write:
        fig.savefig('%s/%s_loop_%s.%s' % (dir_write, recording, j, 'jpg'), dpi = 200, facecolor='w',
            edgecolor='w', orientation='portrait', papertype=None, format = 'jpg',
            transparent=False, bbox_inches=None, pad_inches=0.1, frameon=True)
