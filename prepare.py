# Dataframe maniuplations
import pandas as pd
import numpy as np
# Splitting function
from sklearn.model_selection import train_test_split
# Imputer
from sklearn.impute import SimpleImputer

def prepare_zillow(df):
    '''
    This function takes in the dataframe and returns the train, validate, and test dataframe splits.
    It drops the nulls prior to the split.
    '''
    # Drop the null values
    df = df.dropna()
    train, validate, test = zillow_split(df)
    return train, validate, test


def prepare_zillow_l(df):
    '''
    '''
    # Removal of columns that compromise integrity of target variable
    df = df.drop(columns= ['landtaxvaluedollarcnt', 'structuretaxvaluedollarcnt', 'taxamount'])
    # Removal of columns that have very high null ratio
    for col in df:
        if df[col].isna().sum() >= (.25 * len(df)):
            df = df.drop(columns = col)
    # Dropping rows with null values out of remaning columns
    df = df.dropna()
    # Dropping redundant, unnecessary, or faulty columns
    df = df.drop(columns = ['parcelid', 'propertylandusetypeid', 'calculatedbathnbr', 'finishedsquarefeet12', 'fullbathcnt',
                            'latitude', 'longitude', 'propertycountylandusecode', 'rawcensustractandblock',
                            'roomcnt', 'regionidzip', 'assessmentyear', 'censustractandblock', 'logerror', 
                            'propertylandusedesc', 'regionidcounty'])
    






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


