# Explore

# Dataframe manipulations
import pandas as pd
import numpy as np

# Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Stats
from scipy.stats import pearsonr, f_oneway


def linear_tests(train, conts):
    '''
    This function takes our train dataframe and a list of continous variables and outputs a jointplot, lmplot, and pearsonr hypothesis test.
    There is no return but there is a print statement of whether the null hypothesis is rejecting or accepted.
    '''
    # Looping through the chosen continuous variables
    for col in conts:
        # Creation of a jointplot using our target variable and the selected column
        sns.jointplot(y='tax_value', x=col, data=train, kind='scatter')
        plt.xlabel(f'{col}')
        plt.ylabel('Tax Value')
        plt.show()
        # Creation of a lmplot using our target variable and the selected column
        sns.lmplot(x=col, y='tax_value', data=train, scatter=True, hue=None, col=None)
        plt.xlabel(f'{col}')
        plt.ylabel('Tax Value')
        plt.title(f'{col} by Tax Value')
        plt.show()
        # Printing of our hypothesis surrounding the linear relationship between column and target variable
        print(f'H0: There is no linear relationship between {col} and tax value.')
        print(f'HA: There is a linear relationship between {col} and tax value.')
        print('----------------------------------------------------------------')
        # Established alpha
        alpha = .05
        # Pearsonr test to determine r and p values
        r, p = pearsonr(train[col], train.tax_value)
        # Analysis of p value for rejection or acceptance of null hypothesis
        if p < alpha:
            print(f'p-value: {p}\n')
            print('With a p-value below our established alpha we reject the null hypothesis.')
        else:
            print('We fail to reject the null hypothesis.')


def cat_hists(train, cats):
    '''
    This function takes in our train dataframe and categorical columns (encoded fips column). It returns nothing but does print out
    a histplot for each of the fips, and then conducts an ANOVA test to determine if the mean tax values by location are equal. It prints out
    the hypotheses as well as rejection or acceptance of the null hypothesis.
    '''
    # Looping through our categorical columns (fips encoded)
    for col in cats:
        # Isolation of tax values per county
        h = train[['tax_value', col]]
        h = h[h[col] == 1]
        # Creation of labeled histplot for each individual fip
        hg = sns.histplot(data=h.tax_value)
        hg.set(xlabel='Tax Value', ylabel='Quantity of Houses', title=(f'{col}'))
        plt.show()
    # Testing if mean tax value of all the fips are equal using ANOVA
    # Establishing our alpha
    alpha = .05
    # Establishing our hypotheses
    print('H0: The tax value means of the three fips locations are all equal.')
    print('HA: The tax value means of the three fips locations are not equal.')
    print('------------------------------------------------------------------')
    # Conducting our ANOVA test
    f, p = f_oneway(train.tax_value[train.fips_06037 == 1], train.tax_value[train.fips_06059 == 1], train.tax_value[train.fips_06111 == 1])
    if p < alpha:
        print(f'p-value: {p}\n')
        print('With a p-value below our established alpha we reject the null hypothesis.')
    else:
        print('We fail to reject the null hypothesis.')


def heatmap_zillow(train):
    '''
    This function takes in our train dataframe and creates a correlation from it. This correlation is then mapped as a heatmap.
    '''
    # Creation and mapping of the correlation
    corr = train.corr()
    # Separating the top half of the heatmap to laster mask
    matrix = np.triu(corr)
    plt.figure(figsize=(16,9))
    ax = sns.heatmap(corr, cmap='coolwarm', mask=matrix)
    ax.set(title='Heatmap')


def scaled_relplot(train, conts):
    '''
    This function takes in our train dataframe and a list of continuous features. It then plots relplot (line) graphs of the data.
    '''
    # Looping through the list to form the relplots
    for col in conts:
        sns.relplot(y='tax_value', x=col, data=train, kind='line').set(title=(f'Tax Value by {col}'))
        plt.show()