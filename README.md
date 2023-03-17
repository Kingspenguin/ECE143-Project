# ECE143-Project
 
 
### Dataset Links

1. The World Happiness Report and life expectancy data: 
(https://worldhappiness.report/ed/2020/#appendices-and-data )
and  (https://www.kaggle.com/datasets/mathurinache/world-happiness-report)

2. Social support dataset from the Organisation for Economic Co-operation and Development: https://data.oecd.org/healthrisk/social-support.htm


### File Structure

1. Dataset Folder: Contains all the .csv and .xslx files used for the purpose of the project.
    - Some of the files are downloaded from the links
    - Some of the files were created during data preparation or data merging
2. Python Folder: Contain all the .py files. Some files are solely for the use of data preparations and others are for visualization
    - Data Preparation.py: Creates the 'Happiness_data_from_2015_to_2022.csv' file that we mainly use for analysis and creating visualization.
    - Dataset Merging For COVID.py: Add mortality rates and COVID data to create the 'mortality_merged.csv' file.
    - COVID data analysis.py: Performs mathematical analysis on the 'mortality_merged.csv' file to create the 'COVID_Analysis_Dataset.csv' file.
    - Correlation Matrix Visualization.py: Creates the correlation matrix plot based on the .csv files we created.
3. notebooks Folder: Contains the jupyter notebook with all the visualization used in the presentation.


### How to Run

1. Run the 'Data Preparation.py' to create the 'Happiness_data_from_2015_to_2022.csv' file, which contains all merged happiness data from every year with all the necessary columns. 
    - It uses happiness score datasets from every year to create this file, which are all found in Datasets Folder.
2. Then run the 'Dataset Merging For COVID.py' file, which uses the previously created file and 'mortality_data.xlsx' to create 'mortality_merged.csv' file. 
    - This new .csv file created is used for analyzing COVID and mortality rate data in relation to happiness score.
3. Then run the 'COVID data analysis.py', which uses the previously to .csv files we created to make the 'COVID_Analysis_Dataset.csv'.
    - This is the result of doing mathematical analysis on the .csv file and using this to create visualizations.
4. After all the .csv file is created move them in the dataset folder and run all the visualization.py files to create the graphs
5. Run jupyter notebook to see all the visualization and graphs created for the project.


### Third-party Modules Used

1. Numpy
2. Pandas
3. matplotlib.pyplot
4. seaborn 
5. plotly
6. os
7. csv
8. folium
9. geopandas 
10. sklearn.preprocessing




