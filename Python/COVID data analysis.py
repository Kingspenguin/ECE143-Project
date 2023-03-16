# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:44:23 2023

@author: navid
"""

import pandas as pd


df_2015_2022 = pd.read_csv("../Datasets/Happiness_data_from_2015_to_2022.csv")
df_mortality = pd.read_csv("./mortality_merged.csv")
df_sub = df_2015_2022.loc[:,["Country","year","Happiness Score"]]
df_sub = df_sub[df_sub["year"]<2019]
#df_sub = df_sub[df_sub["year"]>2020]

new_df = df_sub.pivot(index='Country', columns='year', values='Happiness Score')
new_df = new_df.reset_index()
new_df = new_df.rename(columns={'index': 'Country'})
new_df.columns = ['Country', 'Happiness Score 2015', 'Happiness Score 2016', 'Happiness Score 2017','Happiness Score 2018']
merged_mortality_df = pd.merge(df_mortality, new_df, on=['Country'], how='inner')
#merged_mortality_df['2021-2022'] = merged_mortality_df['Happiness Score 2022'] - merged_mortality_df['Happiness Score 2021']
#merged_mortality_df['2020-2021'] = merged_mortality_df['Happiness Score 2021'] - merged_mortality_df['Happiness Score 2020']
merged_mortality_df['2019-2020'] = merged_mortality_df['Happiness Score 2020'] - merged_mortality_df['Happiness Score 2019']
merged_mortality_df['2018-2019'] = merged_mortality_df['Happiness Score 2019'] - merged_mortality_df['Happiness Score 2018']
merged_mortality_df['2017-2018'] = merged_mortality_df['Happiness Score 2018'] - merged_mortality_df['Happiness Score 2017']
merged_mortality_df['2016-2017'] = merged_mortality_df['Happiness Score 2017'] - merged_mortality_df['Happiness Score 2016']
merged_mortality_df['2015-2016'] = merged_mortality_df['Happiness Score 2016'] - merged_mortality_df['Happiness Score 2015']
merged_mortality_df = merged_mortality_df.sort_values(by='Happiness Score 2020', ascending=True)


merged_mortality_df.to_csv('COVID_Analysis_Dataset.csv')
