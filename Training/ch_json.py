# -*- coding: utf-8 -*-
import pandas as pd
import json
import os 

path = os.path.abspath("Data/yelp_academic_dataset_business.json")

data_file = open(path)
df = pd.DataFrame([json.loads(x) for x in data_file.readlines()])
data_file.close()

df.columns

import matplotlib.pyplot as plt
import seaborn as sns

#plot the histogram for the review counts
sns.set_style('whitegrid')
fig, ax = plt.subplots()
df['review_count'].hist(ax= ax, bins =100)
ax.set_yscale('log')
ax.tick_params(labelsize =14)
ax.set_xlabel('Review count', fontsize =14)
ax.set_ylabel('Occurances', fontsize =14)

"""
Quantile binning : Fixed-width binning is easy to compute. But if there are large gaps in the counts, then
there will be many empty bins with no data. This problem can be solved by adaptively
positioning the bins based on the distribution of the data. This can be done using the
quantiles of the distribution.
"""

deciles = df['review_count'].quantile([.1,.2, .3, .4, .5, .6, .7 ,.8 ,.9])

# Visualize the deciles on the histogram
sns.set_style('whitegrid')
fig, ax = plt.subplots()
df['review_count'].hist(ax=ax, bins=100)

for pos in deciles:
    handle = plt.axvline(pos, color='r')
    ax.legend([handle], ['deciles'], fontsize=14)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.tick_params(labelsize=14)
    ax.set_xlabel('Review Count', fontsize=14)
    ax.set_ylabel('Occurrence', fontsize=14)
    
"""
Binning counts by quantiles

"""

# Map the counts to quartiles
large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 44, 28, 7971, 926, 122, 22222]

pd.qcut(large_counts, 4, labels=False)

# Compute the quantiles themselves
large_counts_series = pd.Series(large_counts)
large_counts_series.quantile([0.25, 0.5, 0.75])    