import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import plotly.graph_objs as go
from plotly.offline import iplot
import plotly.express as px
import folium


data_2015=df.loc[df['year'] == 2015]
data_2016=df.loc[df['year'] == 2016]
data_2017=df.loc[df['year'] == 2017]
data_2018=df.loc[df['year'] == 2018]
data_2019=df.loc[df['year'] == 2019]
data_2020=df.loc[df['year'] == 2020]
data_2021=df.loc[df['year'] == 2021]
data_2022=df.loc[df['year'] == 2022]



happy =data_2021
# information to be given when mouse over the country
hover_data = happy[["Happiness Rank","Life Ladder","Freedom to make life choices","Perceptions of corruption","Confidence in national government",
       "Economy (GDP per Capita)","Family",
       "Health (Life Expectancy)","Generosity","Positive affect", "Negative affect"]]
fig = px.choropleth(happy,
                    locations=happy["Country"],
                    locationmode="country names",
                    projection="natural earth",
                    hover_data=hover_data,
                    hover_name=happy["Country"],
                    color="Happiness Score",
                    color_continuous_scale=px.colors.sequential.Rainbow,
                    scope="world")
# fig.show()
fig.update_layout(geo_scope='world',
#                               colorscale=True,
                              title_text='Hapiness Scores in 2021 '
                               )


happy =data_2015
# information to be given when mouse over the country

hover_data = happy[["Happiness Rank","Life Ladder","Freedom to make life choices","Perceptions of corruption","Confidence in national government",
       "Economy (GDP per Capita)","Family",
       "Health (Life Expectancy)","Generosity","Positive affect", "Negative affect"]]
fig = px.choropleth(happy,
                    locations=happy["Country"],
                    locationmode="country names",
                    projection="natural earth",
                    hover_data=hover_data,
                    hover_name=happy["Country"],
                    color="Happiness Score",
                    color_continuous_scale=px.colors.sequential.Rainbow,
                    scope="world")
# fig.show()
fig.update_layout(geo_scope='world',
#                               colorscale=True,
                              title_text='Hapiness Scores in 2015 '
                               )


cols=["Life Ladder","Freedom to make life choices","Perceptions of corruption","Confidence in national government",
       "Economy (GDP per Capita)","Family",
       "Health (Life Expectancy)","Generosity","Positive affect", "Negative affect"]
for a in cols:
    plt.figure(figsize=(10,5))
    plt.title('Happiness Score with Respect to {} in 2021'.format(a))
    sns.regplot(x=a,y='Happiness Score',data=data_2021,color='r')
    plt.savefig('plots_{}_Bivarate.png'.format(a))
#     plt.show()