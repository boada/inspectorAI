import numpy as np
from scipy.ndimage.filters import gaussian_filter

def mk_heatmap(x, y, s, bins=1000):
    ''' Creates a smoothed heatmap given a large set of x,y positions.
    
    x, y -- the data
    s -- the sigma or the number of pixels overwhich to smooth the data
    bins -- the total number of bins across the x and y axes in the image
    
    Returns:
    The smoothed heatmap image
    The image's extent (useful for plotting)
    The bins along the x axis
    The bins along the y axis
    
    '''
    
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[x.min(), x.max()], [y.min(), y.max()]])
    heatmap = gaussian_filter(heatmap, sigma=s)

    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    return heatmap.T, extent, xedges, yedges

def value_heatmap(x, y, xbins, ybins, heatmap):
    ''' Calculates the smoothed value of the heatmap at the given x,y position
    
    x, y -- position to measure the heatmap
    xbins -- the heatmap x bins
    ybins -- the heatmap y bins
    heatmap -- the values of the heatmap
    
    Returns:
    The heatmap's value at the given x, y position.
    
    '''
    
    xbin = np.digitize(x, xbins[1: -1])
    ybin = np.digitize(y, ybins[1: -1])

    return heatmap[ybin][xbin]

def select_by_date(df, start_date, end_date):
    ''' Returns data from the dataframe between two specific dates '''
    
    
    g = df.columns.to_series().groupby(df.dtypes).groups
    type_dict = {k.name: v for k, v in g.items()}
    
    date_col = type_dict['datetime64[ns]'][0]
    
    mask = (df[date_col] > start_date) & (df[date_col] <= end_date)
    
    return df.loc[mask]

def update_grade(y):
    grade_list = ['A','B','C']
    
    if (y.grade in grade_list):
        return y.grade
    elif (y.grade == 'P') | (y.grade == 'Z'):
        if (y.score >= 0) & (y.score <= 13):
            return 'A'
        elif (y.score >= 14) & (y. score <= 27):
            return 'B'
        else:
            return 'C'
    elif not np.isnan(y.score):
        if (y.score >= 0) & (y.score <= 13):
            return 'A'
        elif (y.score >= 14) & (y. score <= 27):
            return 'B'
        else:
            return 'C'
    else:
        return y.grade