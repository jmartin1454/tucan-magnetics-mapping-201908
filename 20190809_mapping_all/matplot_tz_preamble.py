import pytz
tz_PDT = pytz.timezone('America/Vancouver')


import matplotlib as mpl
# mpl.use('Agg')
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

from matplotlib import dates as mdates
xfmt = mdates.DateFormatter('%H:%M', tz=tz_PDT)
