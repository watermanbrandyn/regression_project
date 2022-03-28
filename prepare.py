# Dataframe maniuplations
import pandas as pd
import numpy as np
# Splitting function
from sklearn.model_selection import train_test_split
# Imputer
from sklearn.impute import SimpleImputer

def prepare_zillow(df):
    '''
    '''







def prepare_zillow_l(df):
    '''
    '''
    # Removal of large null columns or ones that compromise integrity of target variable
    df = df.drop(columns= ['airconditioningtypeid', 'architecturalstyletypeid', 'landtaxvaluedollarcnt',
                            'structuretaxvaluedollarcnt', 'taxamount'])
    






def zillow_split(df):
    '''
    This function takes in a dataframe and returns train, validate, test splits. (dataframes)
    An initial 20% of data is split to place as 'test'.
    A second split is performed, on the remaining 80% of original df, to split 70/30 between train and validate. 
    '''
    # First split with 20% going to test
    train_validate, test = train_test_split(df, train_size = .8,
                                            random_state=123)
    # Second split with 70% of remainder going to train, 30% to validate
    train, validate = train_test_split(train_validate, train_size = .7,
                                            random_state=123)
    # Return train, validate, test (56%, 24%, 20% splits of original df)
    return train, validate, test