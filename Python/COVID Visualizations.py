# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:12:34 2023

@author: navid
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Datasets/COVID_Analysis_Dataset.csv")

# create a list of the column names to include in the graph
columns_to_include = ['2015-2016', '2016-2017', '2017-2018', '2018-2019','2019-2020',]

# create a new DataFrame with just the selected columns
df_selected = df[columns_to_include]

# create a new DataFrame to hold the counts of positive and negative values
counts_df = pd.DataFrame(columns=['Score Increase', 'Score Decrease'])

# iterate over the selected columns and count the number of positive and negative values
for col in columns_to_include:
    pos_count = (df_selected[col] > 0).sum()
    neg_count = (df_selected[col] < 0).sum()
    counts_df.loc[col] = [pos_count, neg_count]

# create the bar grap
ax = counts_df.plot(kind='bar', width=0.8, figsize=(11, 8), zorder=2, colormap='Accent')

# set the title and axis labels
ax.set_title('', fontsize=25)
ax.set_xlabel('Time periods', fontsize=20)
ax.set_ylabel('Number of Countries', fontsize=15)
#ax.set_facecolor('#f1f1f1')

# set the x-axis tick labels to the column names
ax.set_xticklabels(columns_to_include, rotation=0, fontsize=18)

# add labels to the bars
for p in ax.containers:
    ax.bar_label(p, label_type='edge', fontsize=20)

# Set the background color of the plot
ax.set_facecolor('#f4fdf4')

# Add a grid to the plot
ax.grid(color='white', linestyle='-', linewidth=1, zorder = 1)    
    
# display the graph
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("../Datasets/COVID_Analysis_Dataset.csv")

# Select the first two columns
cols_of_interest = ['2015-2016', '2016-2017', '2017-2018', '2018-2019','2019-2020']
subset = df[cols_of_interest]

# Calculate the average of each column
avg = subset.mean()

# Create a new figure with a white grid and green background
fig, ax = plt.subplots(figsize=(11, 8))
ax.set_axisbelow(True)
ax.grid(color='white', linestyle='-', linewidth=1)
ax.set_facecolor('#f4fdf4')

# Create a bar plot of the averages with custom colors
colors = ['#30c8c8', '#30a8c8', '#3078c8', '#3048c8', '#3028c8']
plt.bar(avg.index, avg.values, color=colors)

# Set the title and axis labels
plt.title('', fontsize=20)
plt.xlabel('Time Periods', fontsize=20)
plt.ylabel('Average Positive Change in Score', fontsize=15)

# Increase the font size of the tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Display the plot
plt.show()