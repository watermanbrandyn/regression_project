# Dataframe maniuplations
import pandas as pd
import numpy as np
# Splitting function
from sklearn.model_selection import train_test_split
# Imputer
from sklearn.impute import SimpleImputer
# Scaler
from sklearn.preprocessing import MinMaxScaler


def prepare_zillow(df):
    '''
    This function takes a dataframe and then performs a number of preparation steps on it. 
    The nulls are dropped, columns are changed to appropriate datatypes, and a feature is engineered from an old one.
    Additionally, outliers are removed and the categorical column is encoded prior to the data being split into 
    train, validate, and test dataframes. The three dataframes are then returned. 
    '''
    # Removal of null values, represented a small portion of the dataset
    df = df.dropna()
    # Changing fips and yearbuilt to appropriate data types (object)
    # Fips has to be converted to int, str, and concat '0' to properly format number code
    df.fips = df.fips.astype(int)
    df.fips = df.fips.astype(str)
    df.fips = '0' + df.fips
    # Modifying yearbuilt to a more appropriate value, age
    df.yearbuilt = df.yearbuilt.astype(int)
    df['age'] = 2017 - df.yearbuilt
    # Dropping now redundant column yearbuilt
    df = df.drop(columns= 'yearbuilt')
    # Remove the outliers
    df = remove_outliers(df, 1.5, ['bedrooms', 'bathrooms', 'house_area', 'lot_area', 'tax_value'])
    # Encoding the fips column (only categorical column)
    df = pd.get_dummies(df, columns= ['fips'])
    # Splitting the dataframe into three dataframes
    train, validate, test = zillow_split(df)
    # Returning the train, validate, test dataframes
    return train, validate, test

    
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


def remove_outliers(df, k, cols):
    '''
    This function takes in a dataframe, a specified 'k' value (how sensitive to make outlier detection), and a list of 
    columns to remove outliers from. It returns the dataframe without the outliers.
    '''
    # Cycle through specified cols
    for col in cols:
        # Determine the quartiles for each column
        q1, q3 = df[col].quantile([.25, .75])
        # Compute the interquartile range
        iqr = q3 - q1
        # Calculate the upper and lower bounds
        upper_bound = q3 + k * iqr
        lower_bound = q1 - k * iqr
        # Remove the outliers
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        # Return the dataframe without outliers
    return df


def scale_zillow(train, validate, test):
    '''
    This function takes train, validate, and test dataframes and scales their numerical columns that are not
    the target variable. The scaler is fit on the train and then transformed on all three dataframes. Returns the 
    three dataframes.
    '''
    # Identifying which columns will be scaled
    quants = ['bedrooms', 'bathrooms', 'house_area', 'lot_area', 'age']
    # Creation of scaler
    scaler = MinMaxScaler()
    # Fit scaler to train
    scaler.fit(train[quants])
    # Apply to train, validate, and test dataframes
    train[quants] = scaler.transform(train[quants])
    validate[quants] = scaler.transform(validate[quants])
    test[quants] = scaler.transform(test[quants])
    # Return the three scaled dataframes
    return train, validate, test

