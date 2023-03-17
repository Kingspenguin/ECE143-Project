# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:56:34 2023

@author: navid
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objs as go
import plotly.express as px



pivot_df = pd.read_csv('../Datasets/year_happiness_score.csv')
year = 2015

while year<2022:
    pivot_df[str(year)] = pivot_df[str(year)].astype(int)
    year = year + 1
pivot_df['Country'].astype('str')
pivot_df.set_index('Country',inplace=True)

pivot_df = pivot_df.drop('Algeria')
pivot_df = pivot_df.drop('Jordan')
pivot_df = pivot_df.drop('Malaysia')

new_df = pivot_df.diff(axis=1)
new_df = new_df.drop('2015',axis=1)
nd = new_df.le(0).all(axis=1)
countries = new_df[nd].abs().sum(axis=1)
filt_countries = countries.nlargest(6)
coun = filt_countries.index.to_list()
decreasing_ranks = pivot_df.loc[coun]
decreasing_ranks

import plotly.graph_objs as go

dr = decreasing_ranks

pivot_df['diff'] = pivot_df['2021'] - pivot_df['2015']
ir = pivot_df.nlargest(columns='diff',n=5)
ir = ir.drop(columns='diff')

dr = ir
fig = go.Figure()

for country in dr.index:
    fig.add_trace(go.Scatter(x=dr.columns, y=dr.loc[country], name=country,showlegend=False, line=dict(width=2)))
    # if country=='Venezuela':
    #     fig.add_annotation(x=6, y=dr.loc[country]['2021'],text=country,xanchor='left', yanchor='bottom',textangle=360,showarrow=False,font=dict(size=12))
    # else:
    fig.add_annotation(x=6, y=dr.loc[country]['2021'],text=country,xanchor='left', yanchor='middle',textangle=360,showarrow=False,font=dict(size=12))

fig.update_layout(title='Overall decrease in Happiness Rank 2015-2021', xaxis_title='Year', yaxis_title='Happiness Rank')
fig.update_layout(
    yaxis=dict(
        autorange='reversed'
    ))

fig.update_layout(
    width=600,  # Set the width to 800 pixels
    height=800  # Set the height to 600 pixels
)

fig.show()


inr = pivot_df.nsmallest(columns='diff',n=5)
inr = inr.drop(columns='diff')

dr = inr
fig = go.Figure()

for country in dr.index:
    fig.add_trace(go.Scatter(x=dr.columns, y=dr.loc[country], name=country,showlegend=False, line=dict(width=2)))
    fig.add_annotation(x=6.05, y=dr.loc[country]['2021'],text=country,xanchor='left', yanchor='middle',textangle=360,showarrow=False,font=dict(size=12))

fig.update_layout(title='Highest overall increase in Happiness Rank 2015-2021', xaxis_title='Year', yaxis_title='Happiness Rank')
fig.update_layout(
    yaxis=dict(
        autorange='reversed'
    ))

fig.update_layout(
    width=600,  # Set the width to 800 pixels
    height=800  # Set the height to 600 pixels
)

fig.show()

