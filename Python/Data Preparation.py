# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:46:19 2023

@author: navid
"""

import pandas as pd
import numpy as np


df_2015 = pd.read_csv("../Datasets/2015.csv")
df_2015['year'] = 2015
df_new_2015=df_2015[["Country",'year', "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2015.head()
#size (158, 12)

df_2016 = pd.read_csv("../Datasets/2016.csv")
df_2016.head()
df_2016['year'] = 2016
df_new_2016=df_2016[["Country",'year', "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2016.head()
#size(157, 13)
#new colums
#Lower Confidence Interval and Upper Confidence Interval
#  different from 2015 : does not have Standard Error

df_2017 = pd.read_csv("../Datasets/2017.csv")

df_2017.rename(columns={"Happiness.Rank": "Happiness Rank"}, inplace=True)
df_2017.rename(columns={"Happiness.Score": "Happiness Score"}, inplace=True)
df_2017.rename(columns={"Economy..GDP.per.Capita.": "Economy (GDP per Capita)"}, inplace=True)
df_2017.rename(columns={"Health..Life.Expectancy.": "Health (Life Expectancy)"}, inplace=True)
df_2017.head()
df_2017['year'] = 2017
df_new_2017=df_2017[["Country",'year', "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2017.head()
#size (155, 12)
#new colums no from 2016 , but the name change and order of the colum
#  different from 2015 : does not have Standard Error and Region

df_2018 = pd.read_csv("../Datasets/2018.csv")
df_2018.rename(columns={"Overall rank": "Happiness Rank"}, inplace=True)
df_2018.rename(columns={"Country or region": "Country"}, inplace=True)
df_2018.rename(columns={"Score": "Happiness Score"}, inplace=True)
df_2018.rename(columns={"GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2018.rename(columns={"Healthy life expectancy": "Health (Life Expectancy)"}, inplace=True)
df_2018.rename(columns={"Social support": "Family"}, inplace=True)
df_2018.head()
df_2018['year'] = 2018
df_new_2018=df_2018[["Country",'year', "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2018.head()

#size (156, 9)
#new no colums no but the name change and order of the colum
#  different from 2015 : does not have Standard Error and Region
#   different from 2016 and 2017 :does not have Trust..Government.Corruption. and Whisker.high	Whisker.low 

df_2019 = pd.read_csv("../Datasets/2019.csv")
df_2019.rename(columns={"Overall rank": "Happiness Rank"}, inplace=True)
df_2019.rename(columns={"Country or region": "Country"}, inplace=True)
df_2019.rename(columns={"Score": "Happiness Score"}, inplace=True)
df_2019.rename(columns={"GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2019.rename(columns={"Healthy life expectancy": "Health (Life Expectancy)"}, inplace=True)
df_2019.rename(columns={"Social support": "Family"}, inplace=True)
df_2019['year'] = 2019
df_new_2019=df_2019[["Country",'year', "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2019.head()
#size (156, 9)
#new no colums no but the name change and order of the colum
#  different from 2015 : does not have Standard Error and Region
#   different from 2016 and 2017 :does not have Trust..Government.Corruption. and Whisker.high	Whisker.low

df_2020 = pd.read_csv("../Datasets/2020.csv")
#df_2020.rename(columns={"Overall rank": "Happiness Rank"}, inplace=True)
df_2020.rename(columns={"Country name": "Country"}, inplace=True)
df_2020.rename(columns={"Ladder score": "Happiness Score"}, inplace=True)
df_2020.rename(columns={"Logged GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2020.rename(columns={"Healthy life expectancy": "Health (Life Expectancy)"}, inplace=True)
df_2020.rename(columns={"Social support": "Family"}, inplace=True)
df_2020.head()
df_2020['year'] = 2020
df_2020['Happiness Rank'] = range(1, len(df_2020)+1)
df_new_2020=df_2020[["Country",'year','Happiness Rank',"Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2020.head()
#size (153, 20)
# alot of extra colum 
# but the name change and order of the colum

df_2021 = pd.read_csv("../Datasets/2021.csv")
df_2021.head()

df_2021.rename(columns={"Country name": "Country"}, inplace=True)
df_2021.rename(columns={"Ladder score": "Happiness Score"}, inplace=True)
df_2021.rename(columns={"Logged GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2021.rename(columns={"Healthy life expectancy": "Health (Life Expectancy)"}, inplace=True)
df_2021.rename(columns={"Social support": "Family"}, inplace=True)
df_2021.head()
df_2021['year'] = 2021
df_2021['Happiness Rank'] = range(1, len(df_2021)+1)
df_new_2021=df_2021[["Country","year","Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_2021.head()
#size (149, 20)
# alot of extra colum 
# but the name change and order of the colum

df_2022 = pd.read_csv("../Datasets/2022.csv")
df_2022.head()

df_2022 = pd.read_csv("../Datasets/2022.csv")

df_2022.rename(columns={"RANK": "Happiness Rank"}, inplace=True)
df_2022.rename(columns={"Happiness score": "Happiness Score"}, inplace=True)
df_2022.rename(columns={"Explained by: Generosity": "Generosity"}, inplace=True)
df_2022.rename(columns={"Explained by: GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2022.rename(columns={"Explained by: GDP per capita": "Economy (GDP per Capita)"}, inplace=True)
df_2022.rename(columns={"Explained by: Healthy life expectancy": "Health (Life Expectancy)"}, inplace=True)
df_2022.rename(columns={"Explained by: Social support": "Family"}, inplace=True)
df_2022.head()
df_2022['Health (Life Expectancy)'] = df_2022['Health (Life Expectancy)'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
df_2022['Health (Life Expectancy)'] = df_2022['Health (Life Expectancy)'].apply(lambda x: (x)*100)

df_2022['Happiness Score'] = df_2022['Happiness Score'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
df_2022['Family'] = df_2022['Family'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
df_2022['Generosity'] = df_2022['Generosity'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
df_2022['Economy (GDP per Capita)'] = df_2022['Economy (GDP per Capita)'].apply(lambda x: float(x.replace(',', '.')) if isinstance(x, str) else x)
df_2022['year'] = 2022

#df_2022.to_csv('df_new_2022.csv', index=False)
#df_df = pd.read_csv("../notebooks/df_new_2022.csv")
df_new_22=df_2022[["Country","year", "Happiness Rank","Happiness Score","Economy (GDP per Capita)","Family","Health (Life Expectancy)","Generosity"]]
df_new_22.head()
#size (149, 20)
# simarl to 2016 and 2017 
# but the name change and order of the colum
#  different from 2015 : does not have Standard Error and Region

# Combine data frames using `concat` function
combined_df = pd.concat([df_new_2015, df_new_2016, df_new_2017,df_new_2018,df_new_2019,df_new_2020,df_new_2021,df_new_22])

# Display the combined data frame
print(combined_df)
combined_df.to_csv('Happiness_data_from_2015_to_2022.csv', index=False)


