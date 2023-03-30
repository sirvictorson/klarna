"""
UTILS 
- Helper functions to use for predictionfunctions, etc
- Data: import files/models e.g.
- Models:
    - best_model: trained sklearn classification model
"""
import pandas as pd
import numpy as np

predicted = pd.read_csv('./data/prediction.csv', sep=';')

def get_pred(userid):
    mask = predicted['uuid'] == userid
    default = predicted.loc[mask, 'pd'].tolist()[0]
    return default

