from os import listdir
from os.path import isfile, join

import numpy as np
import pandas as pd
from scipy import stats

# Import matplotlib and pyplot for plotting
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt
import matplotlib.ticker 

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 14, 'axes.titlesize': 14}
sns.set(rc=rc)

# define an ecdf function
def ecdf(data):
    return np.sort(data), np.arange(1, len(data)+1) / len(data)

df_scSPRITE_1min = pd.read_csv('one_last_time_sort_reads.txt', delimiter='\t', header=None, index_col=False, low_memory=False)
#int(df_scSPRITE_1min[2][1])

def cumulative(df, column):
    df_cumulative = []
    total = 0
    track = 0

    for read in range(len(df)-1):
        total = total + int(df[column][read])

    for read in range(len(df)-1):
        if read == 0:
            track = int(df[column][read])
            df_cumulative.append(track/total)
        else:
            track = track + int(df[column][read])
            df_cumulative.append(track/total)
    return df_cumulative

def cumulative_notnorm(df, column):
    df_cumulative = []
    total = 0
    track = 0

    for read in range(len(df)-1):
        total = total + int(df[column][read])

    for read in range(len(df)-1):
        if read == 0:
            track = int(df[column][read])
            df_cumulative.append(track)
        else:
            track = track + int(df[column][read])
            df_cumulative.append(track)
    return df_cumulative

reads_cumulative = cumulative_notnorm(df_scSPRITE_1min, 2)
cluster_cumulative = cumulative_notnorm(df_scSPRITE_1min, 1)

plt.plot(reads_cumulative, marker='.', color='b', linestyle='none')

plt.legend(['Reads', 'Clusters'], loc=4, fontsize=10, markerscale=2)
plt.margins(y=1)
plt.xlabel('Unique Barcode', fontsize=12)
plt.ylabel('Cumulative sum', fontsize=12)

#plt.ylim(1,100000000)
# plt.xlim(1, 1700)
plt.semilogy()
plt.semilogx()

plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# draw vertical line 
# plt.plot([75, 75], [0, 1], 'r-', lw=2)
# plt.plot([1, 1], [0, 1], 'k-', lw=2)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# fig.text(0.44, 0.65, '99% of cell barcode IDs identify \n75 clusters or less per ID', fontsize=20,
#         verticalalignment='top', bbox=props)
plt.title('Cumulative sorting of reads & clusters\n(sorting reads from highest to lowest)', fontsize=16)
plt.savefig('myplot1.png')
plt.close()

reads_cumulative_norm = cumulative(df_scSPRITE_1min, 2)
cluster_cumulative_norm = cumulative(df_scSPRITE_1min, 1)

plt.plot(reads_cumulative_norm, marker='.', color='b', linestyle='none')
plt.plot(cluster_cumulative_norm, marker='.', color='r', linestyle='none')

plt.legend(['Reads', 'Clusters'], loc=4, fontsize=10, markerscale=2)
plt.margins(y=1)
plt.xlabel('Unique Barcode', fontsize=12)
plt.ylabel('Cumulative distribution', fontsize=12)
plt.ylim(0,1)
# plt.xlim(290000, 320000)
# plt.semilogx()
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# draw vertical line 
# plt.plot([75, 75], [0, 1], 'r-', lw=2)
# plt.plot([1, 1], [0, 1], 'k-', lw=2)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# fig.text(0.44, 0.65, '99% of cell barcode IDs identify \n75 clusters or less per ID', fontsize=20,
#         verticalalignment='top', bbox=props)
plt.title('Normalized cumulative distribution of reads & clusters', fontsize=16)
plt.savefig('myplot2.png')
plt.close()

#to_plot = cumulative(df_reads)

plt.plot(cluster_cumulative_norm, marker='.', color='b', linestyle='none')

# plt.legend(['20181203', '20180830'], loc=4, fontsize=16)
plt.margins(y=1)
plt.xlabel('Unique Barcode', fontsize=12)
plt.ylabel('Cumulative fraction of clusters', fontsize=12)
plt.ylim(0,1)
plt.xlim(0, 2000)
# plt.semilogx()
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# draw vertical line 
plt.plot([1580, 1580], [0, 1], 'r-', lw=2)
# plt.plot([1, 1], [0, 1], 'k-', lw=2)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# fig.text(0.44, 0.65, '99% of cell barcode IDs identify \n75 clusters or less per ID', fontsize=20,
#         verticalalignment='top', bbox=props)
#fig.text(0.44, 0.45, 'the largest 1580 barcodes make up\n94% of all clusters present', fontsize=16,
#        verticalalignment='top', bbox=props)
plt.title('Normalized cumulative fraction of clusters', fontsize=16)
plt.savefig('myplot3.png')
plt.close()

plt.plot(reads_cumulative_norm, marker='.', color='b', linestyle='none')

# plt.legend(['20181203', '20180830'], loc=4, fontsize=16)
plt.margins(y=1)
plt.xlabel('Unique Barcode', fontsize=12)
plt.ylabel('Cumulative distrbution of reads', fontsize=12)
plt.ylim(0,1)
plt.xlim(1, 2000)
# plt.semilogx()
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

# draw vertical line 
# plt.plot([75, 75], [0, 1], 'r-', lw=2)
# plt.plot([1, 1], [0, 1], 'k-', lw=2)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# fig.text(0.44, 0.65, '99% of cell barcode IDs identify \n75 clusters or less per ID', fontsize=20,
#         verticalalignment='top', bbox=props)
plt.title('Normalized cumulative distribution of reads\n(sorting reads from highest to lowest)', fontsize=16)
plt.savefig('myplot4.png')
plt.close()


