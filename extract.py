# this file will handle extracting the data and populating the initial
# data table with the raw data

import pandas as pd
import numpy as np
from scipy import stats

class Data:
    def __init__(self, filename):
        self.filename = filename
        self.df = None # the dataframe returned by pd
        self.data = None # a list of tuples containing the raw data
        self.get_data(self.filename)
        self.preprocess()

    # get dataframe from csv
    def get_data(self, filename):
        self.df = pd.read_csv(f'{filename}') 
    
    def preprocess(self):
        cols_to_include = ['Age', 'Usage Frequency', 'Support Calls', 'Payment Delay', 'Subscription Type', 
                           'Contract Length', 'Total Spend', 'Last Interaction', 'Churn']
        self.df = self.df[cols_to_include] # extract only the columns to include
        self.df = self.df.dropna() # drop any rows with empty column values

        self.remove_outliers('Age')
        self.remove_outliers('Usage Frequency')
        self.remove_outliers('Total Spend')
        self.remove_outliers('Support Calls', 3)
        self.remove_outliers('Last Interaction', 3)
        self.normalize('Total Spend')
        self.normalize('Last Interaction')

        self.data = [tuple(row) for row in self.df.values] # convert data


    # uses the z score to identify and remove outliers
    def remove_outliers(self, column, threshold=2):
        # set threshold to 2
        z_scores = np.abs(stats.zscore(self.df[column])) # get z-scores for column
        self.df = self.df[z_scores <= threshold] # filter outliers

    # min max normalize
    def normalize(self, column):
        min = self.df[column].min()
        max = self.df[column].max()
        self.df[column] = (self.df[column] - min) / (max - min)

    