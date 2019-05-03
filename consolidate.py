import pandas as pd
import csv
import os

# Created an iterable list of csvs
folder = [os.path.relpath(x) for x in os.listdir('dir')]

# Created a string object containing the folder location to dump the files into
root = 'dir'

# Loops through each file, adds a new column with values containing orig. filename
for file in folder:
    df = pd.read_csv('dir'+file, header=0, index_col=0)
    o = os.path.basename(file)
    df['Original Filename'] = o
    df.to_csv(root + '/' + file) # saves to designated root folder


# created an iterable list of the csv's with the original filename column
root2 = [os.path.relpath(x) for x in os.listdir('dir')]


# Combines all csv's into a dataframe
combined_csv = pd.concat([pd.read_csv('dir'+f) for f in root2], sort=False)

# loads combined csvs into a file
combined_csv.to_csv("combined_csv.csv", index=0)
