# -*- coding: UTF-8 -*-

##
## Definition of Allan deviation is standard one in text boooks 
##

def allan(xd, k):
    import numpy as np
    M = len(xd) // k
    if k==1:
        yd = np.array([ np.average(xd[i:i+k]) for i in range(M)]) 
    else:
        yd = np.array([ np.average(xd[k*i:k*(i+1)])  for i in range(M)])
    dyd = np.diff(yd)
    dyd2 = dyd * dyd
    sigmaA = np.sqrt(1.0/(2*(M-1.0))* np.sum(dyd2))
    return sigmaA

def allan_werr(xd, k):
    import numpy as np
    M = len(xd) // k
    if k==1:
        yd = np.array([ np.average(xd[i:i+k]) for i in range(M)]) 
    else:
        yd = np.array([ np.average(xd[k*i:k*(i+1)])  for i in range(M)])
    dyd = np.diff(yd)
    dyd2 = dyd * dyd
    sigmaA = np.sqrt(1.0/(2*(M-1.0))* np.sum(dyd2))
    #sigmaA = np.sqrt(1.0/((M-1.0))* np.sum(dyd2))
    return sigmaA, sigmaA/np.sqrt(2*(M-1))
    
def allanArray(xd, N):
    import numpy as np
    result = []
    for i in range(N)[1:]:
        result.append(allan(xd, i))
    resd = np.array(result)
    return resd

def LVtime_convert(LVtime):
    from pandas import to_datetime, DataFrame, DatetimeIndex
    import numpy as np
    df_t = DataFrame(LVtime, columns=['LVtime'])
    dtLU = 2082844800
    df_t['datetime'] = (DatetimeIndex(to_datetime((df_t['LVtime'] - dtLU) * 1e9)).tz_localize('UTC')).tz_convert('CET')
    
    return np.array(df_t['datetime'])


import matplotlib as mpl

mpl.rcParams['lines.linewidth'] = 0.8
mpl.rcParams['figure.figsize'] = [8.0, 6.0]
mpl.rcParams['figure.dpi'] = 80
mpl.rcParams['savefig.dpi'] = 100

mpl.rcParams['font.size'] = 10
mpl.rcParams['legend.fontsize'] = 'medium'
mpl.rcParams['figure.titlesize'] = 'medium'
mpl.rcParams['font.family'] = 'sans-serif'
#mpl.rcParams['font.sans-serif'] = 'Helevetica'

mpl.rcParams['timezone'] = 'America/Vancouver'
