# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:32:01 2023

@author: navid
"""

import pandas as pd

# read the csv files 
df = pd.read_csv("../Datasets/all_years_happiness_data.csv")
df = df.drop(columns=["Log GDP per capita", "Social support", "Healthy life expectancy at birth", "Generosity"])
df.columns

# checking how many null values are there in each column
df.isnull().sum()

# make a new dataframe that stores entries from 2014 onwards only 
df_main = df[df['year']>2014]

# rename some columns 
df_main = df_main.rename(columns={'Country name': 'Country'})

df_2015_2022 = pd.read_csv("../Datasets/Happiness_data_from_2015_to_2022.csv")
df_2015_2022


# this merges the data cleaned by Afnan with the dataset already present, so there are more variables we can have now

merged_df = pd.merge(df_main, df_2015_2022, on=['Country', 'year'], how='inner')
merged_df.to_csv("final_merged_data11.csv")

merged_df

# reading in the mortality data 

df_mortality = pd.read_excel("../Datasets/mortality_data.xlsx")
df_mortality = df_mortality.drop(columns=["Female head of government"])
df_mortality = df_mortality.rename(columns={"Country name": "Country"})

# add happiness score and rank to these entries 
df_sub = df_2015_2022.loc[:,["Country","year","Happiness Score"]]
df_sub = df_sub[df_sub["year"]>2018]
df_sub = df_sub[df_sub["year"]<2021]

# now make 2 columns based on years
new_df = df_sub.pivot(index='Country', columns='year', values='Happiness Score')
new_df = new_df.reset_index()
new_df = new_df.rename(columns={'index': 'Country'})
new_df.columns = ['Country', 'Happiness Score 2019', 'Happiness Score 2020']


# merge the two dataframes based on country 

merged_mortality_df = pd.merge(df_mortality, new_df, on=['Country'], how='inner')
merged_mortality_df.to_csv("mortality_merged.csv")
merged_mortality_df
