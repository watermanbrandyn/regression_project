# Predicting Tax Value, Zillow (Regression Project)

## Table of Contents
- [Project Goal](#project-goal)
- [Project Description](#project-description)
- [How to Reproduce](#how-to-reproduce)
- [Initial Questions](#initial-questions)
- [Data Dictionary](#data-dictionary)
- [Project Plan](#project-plan)
   - [Wrangling](#wrangling)
      - [Acquire](#acquire)
      - [Preparation and Splitting](#preparation-and-splitting)
  - [Exploration](#exploration)
  - [Modeling](#modeling)
  - [Deliverables](#deliverables)
    - [Final Report](#final-report)
    - [Modules](#modules)
    - [Predictions](#predictions)
- [Summary and Recommendations](#summary-and-recommendations)

## Project Goal
The goal of this project is to offer analysis to Zillow that can help predict the tax values ($) for Single Family Properties. 
This will be done by identifying some of the key attributes that drive tax value, creating models to help predict this value (using these key attributes), and offering recommendations to assist Zillow in making these predictions moving forward.  

## Project Description
There are a number of factors that can influence the tax value of a property. These can range from physical attributes of the property, individual actions of property owners (such as remodeling choices), or even the decisions made by local, state, or federal entities. This complex web of interactions can certainly make for a difficult task when trying to predict a tax value, but the ability to do so will be greatly beneficial to both Zillow and their clients. 

Through the identification of key drivers, application of these drivers to models, and the testing of prediction capabilities we can help Zillow obtain an advantage in the acquistion and sales of real-estate. This in turn can help Zillow attain a reputation of having a better understanding of the volatility behind pricing, and ensure the company remains a leader in both consultation regarding, and movement of, the housing marketplace. 

## How to Reproduce - (Not Done)
To reproduce the outcomes in this project:
1. Have an env.py file with credentials (hostname, username, password) to access a SQL database that contains Telco data. Codeup's 'telco_churn' data was utilized
   for this project. 
2. Clone this repo and ensure you have all of the necessary modules and notebooks. Confirm that the .gitignore includes your env.py file to secure credentials.
3. Use of these libraries: pandas, numpy, matplotlib, seaborn, sklearn.
4. Be able to run the 'Final Report' jupyter notebook file. 
   - Supplemental 'classification_workbook' may also be useful in identifying some of the steps taken prior to the cleaner final code 

## Initial Questions
_What is our minimum viable product? (MVP)_
- At a minimum this project aims to provide:
   - An explanation of several key drivers of tax value.
   - At least one model that can perform better than a baseline prediction of tax value.
   - At least two recommendations for Zillow on how to predict tax value moving forward.

_Initial Data Centric Questions_
- How do we define 'Single Family Properties'? 
- What is our best method for a baseline prediction of tax value (mean, median, mode)?
   - What is our baseline prediction of tax value?
- How do our core physical attributes impact tax value?
   - Square feet, Bedrooms, Bathrooms 
- How do our add-on components impact tax value?
   - Examples: Pools, Decks, Type of Heating/Cooling, etc...
- How do immutable attributes impact tax value?
   - Examples: Geographic location (State, County, Zipcode, Neighborhood), Year Built, etc...

_Initial Business Questions_
- What are the main drivers and which are not as important in tax value predictions?
- In what ways can this knowledge benefit Zillow and their clients? 

_Initial Hypotheses_
- Is there a linear relationship between tax value and our core physical attributes? (Three separate Pearson investigations)
- Is there a difference in tax values by geographic attributes? (Various T-Test/ANOVA investigations)
- Is there independence between tax value and add-on components? (Various Chi-Square investigations)

## Data Dictionary (Not Done)
| Attribute                             | Definition                                      | Data Type | Additional Info    |
|:--------------------------------------|:------------------------------------------------|:---------:|:-------------------|
| customer_id                           | Unique ID for each customer                     | object    | Format: 0000-AAAAA |
| senior_citizen                        | If customer is a senior                         | int64     | 0: No, 1: Yes      |
| tenure                                | Duration customer has been with Telco           | int64     | In months, 1-72    |
| monthly_charges                       | Total in $ a customer pays each month           | float64   | Range: 18.25-118.75 | 
| total_charges                         | Total in $ of customer to date                  | float64   | Range: 18.80-8684.80 |
| gender_Male                           | If customer is a male                           | uint8     | 0: No, 1: Yes      |  
| partner_Yes                           | If customer has a partner                       | uint8     | 0: No, 1: Yes      |  
| dependents_Yes                        | If customer has dependents                      | uint8     | 0: No, 1: Yes      |  
| phone_service_Yes                     | If customer has phone service                   | uint8     | 0: No, 1: Yes      |  
| multiple_lines_No phone service       | If customer has multiple phone lines (no phone) | uint8     | 0: No, 1: Yes      |  
| multiple_lines_Yes                    | If customer has multiple phone lines            | uint8     | 0: No, 1: Yes      |  
| online_security_No internet service   | If customer has online security (no internet)   | uint8     | 0: No, 1: Yes      |  
| online_security_Yes                   | If customer has online security                 | uint8     | 0: No, 1: Yes      |   
| online_backup_No internet service     | If customer has online backup (no internet)     | uint8     | 0: No, 1: Yes      |  
| online_backup_Yes                     | If customer has online backup                   | uint8     | 0: No, 1: Yes      |  
| device_protection_No internet service | If customer has device protection (no internet) | uint8     | 0: No, 1: Yes      | 
| device_protection_Yes                 | If customer has device protection               | uint8     | 0: No, 1: Yes      |  
| tech_support_No internet service      | If customer has tech support (no internet)      | uint8     | 0: No, 1: Yes      |  
| tech_support_Yes                      | If customer has tech support                    | uint8     | 0: No, 1: Yes      |  
| streaming_tv_No internet service      | If customer has streaming tv (no internet)      | uint8     | 0: No, 1: Yes      |  
| streaming_tv_Yes                      | If customer has streaming tv                    | uint8     | 0: No, 1: Yes      |  
| streaming_movies_No internet service  | If customer has streaming movies (no internet)  | uint8     | 0: No, 1: Yes      |  
| streaming_movies_Yes                  | If customer has streaming movies                | uint8     | 0: No, 1: Yes      |  
| paperless_billing_Yes                 | If customer has paperless billing               | uint8     | 0: No, 1: Yes      |  
| churn_Yes                             | If customer has churned                         | uint8     | 0: No, 1: Yes      |  
| internet_service_type_Fiber optic     | If customer has Fiber for internet service      | uint8     | 0: No, 1: Yes      |  
| internet_service_type_None            | If customer does not have internet service      | uint8     | 0: No, 1: Yes      |  
| contract_type_One year                | If customer contract is for one year            | uint8     | 0: No, 1: Yes      |  
| contract_type_Two year                | If customer contract is for two years           | uint8     | 0: No, 1: Yes      |  
| payment_type_Credit card (automatic)  | If customer payment type is credit card (auto)  | uint8     | 0: No, 1: Yes      |  
| payment_type_Electronic check         | If customer payment type is electronic check    | uint8     | 0: No, 1: Yes      |  
| payment_type_Mailed check             | If customer payment type is mailed check        | uint8     | 0: No, 1: Yes      |

Not shown but present through encoding: internet_service_type_DSL, contract_type_none (Month to month), payment_type_Bank transfer (auto)

## Project Plan (Not Done)
This project will start with some initial planning and question exploration before we even access the data. The question exploration has been delved out in the _Initial Questions_ section. 
Additionally let us detail what is to be provided at the conclusion of this project:
 - This README.md
 - Final Report.ipynb 
 - Workbooks and modules used

Moving forward we will **wrangle (acquire/prepare)** our data, **explore** for insights on key drivers, create **models** for prediction, and apply the best ones for the purpose of curating some **predictions**. This will all be **summarized** and **recommendations** for Telco will be provided. 
For a more detailed breakdown of these steps please see the Final Report and workbooks provided. 

### Wrangling (Not Done)
This section contains our acquisition and preparation of the data.
#### Acquire (Not Done)
The acquire.py file contains the code that was used for acquiring the 'telco_churn' data. There is a **get_db_url()** function that is used to format the credentials for interacting with a SQL server, and the **get_telco_data()** function that queries the SQL server for the data. For this project Codeup's 'telco_churn' SQL database was used. The env.py file used, and the credentials within, are not included in this project and as covered under _How To Reproduce_ must be curated with one's own information.

#### Preparation and Splitting (Not Done)
The prepare.py file contains the code that was used for preparing the data. There is a **telco_split()** function that is used to create a train, validate, and test splits (3 dataframes) of the prepared dataframe. These splits are 56% train, 24% validate, and 20% test from the prepared dataframe. The **prep_telco()** function takes the acquired dataframe and cleans it for our exploratory purposes. Within this function the **telco_split()** function is utilized. 

### Exploration (Not Done)
For exploration we used only our train dataframe. The explore.py file contains a number of functions that were used to help gain insights into our data, using both visual and statistical methods. We delved out the key factors of churn and curating train, validate, and test dataframes to include only these features. The main takeaways from exploration are that churn is most influenced by:
- Fiber service
- Not having a contract
- Electronic check payment
- Tenure (low duration)
- Having a higher monthly cost
- Being a senior citizen

### Modeling (Not Done)
We created a number of models from Decision Tree, Random Forest, K-Nearest Neighbor (KNN), and Logistic Regression types using our selected feature sets. Our report covers the top three performing models (1 KNN, 2 Random Forest) with the best performance being a Random Forest model. From this model we obtained a **90%** accuracy on our test dataframe. This is well above the baseline accuracy of 73% and means that this model should perform well on future unseen data as well.

### Deliverables (Not Done)
The main deliverables from this project are the Final Report and the predictions csv. Additionally there are modules that contain the functions used and workbooks where a deeper exploration of the process can be seen.

#### Final Report (Not Done)
The Final Report can be ran to reproduce the same results from start to finish. 

#### Modules (Not Done)
The modules included in this project are:
- acquire.py
- prepare.py
- explore.py
- model.py

#### Predictions (Not Done)
The random_forest_csv() function in our model module will output the predictions for our test set from our best performing Random Forest model. It contains customer_id, prediction, and prediction probability. 

## Summary and Recommendations (Not Done)
We were successful at identifying some key drivers of churn that were:
- Having Fiber service (Phone and Internet)
- Not having a contract
- Electronic check payment
- Having a low tenure duration
- Having a higher monthly cost
- Being a senior citizen

Moving forward the areas that would be the most impactful for Telco to take action on would be addressing the underlying issues with Fiber satisfaction. This group has the highest liklihood of churn and should be prioritized above all else. Additionally, looking at incentives that could have customers switch from Month to Month payments to a contract (preferably a Two year one) would have a large impact on churn. 



