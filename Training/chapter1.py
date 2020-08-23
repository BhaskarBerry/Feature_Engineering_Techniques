# -*- coding: utf-8 -*-
import pandas as pd
import os
path  = os.path.abspath("Data/taste_profile_song_to_tracks.txt.zip")

#Do note that this will cause the offending lines to be skipped. error_bad_Lines
listen_data  = pd.read_csv(path, header = None, delimiter = "\t", error_bad_lines = False)

data  = pd.read_csv(path, header = None, sep ='delimiter')

col = ['col1','col2','coll3']

data1  = pd.read_csv(path, header = None, delimiter = "\t", names = col)

data1[2]  = 1

"""
Quantizing the count with fixed width bins

"""
import numpy as np

random_num = np.random.randint(0,100,20)
random_num

# Map to evenly spaced bins 0-9 by division
np.floor_divide(random_num, 10)

#An array of counts that span several magnitudes
large_counts = [296, 8286, 64011, 80, 3, 725, 867, 2215, 7689, 11495, 91897, 44, 28, 7971, 926, 122, 22222]

# Map to exponential-width bins via the log function
np.floor(np.log10(large_counts))    

