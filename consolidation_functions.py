# Refactor code here
import pandas as pd
import os

def csvList(root):
    """ Create an iterable list of csv files. """
    files = [os.path.relpath(x) for x in os.listdir(root)]

    return files


def original_filename_col(files, root):
    """ Create a new col with values indicating the original filename and saves to a new folder. """
    new = []
    for file in files:
        df = pd.read_csv(root + file, header=0, index_col=0)
        o = os.path.basename(file)
        df['Original Filename'] = o
        new.append(df)

    return new

def save_changes(save, changes): # save = dir of new folder
    """ Save any changes to a new folder. """
    for c in changes:
        df.to_csv(save + c)


def combine_csvs(save):
    """ Combine a list of similar csvs into a dataframe and save it as one file. """
    r = [os.path.relpath(x) for x in os.listdir(save)]

    combined_csv = pd.concat([pd.read_csv(save + f) for f in r], sort=False)

    combined_csv.to_csv("combined_csv.csv", index=0)
