# ECE143-Project Group 4 An Analysis of The World Happiness Report

### Dataset Links

The World Happiness Report: 
(https://worldhappiness.report/ed/2020/#appendices-and-data )
and  (https://www.kaggle.com/datasets/mathurinache/world-happiness-report)

### How to Run

Clone the repository using 
```
git clone git@github.com:Kingspenguin/ECE143-Project.git
```

Install the dependencies:
```
pip install requirements.txt
```

1. Run the 'Data Preparation.py' to create the 'Happiness_data_from_2015_to_2022.csv' file, which contains all merged happiness data from every year with all the necessary columns. 
    - It uses happiness score datasets from every year to create this file, which are all found in [Datasets](https://github.com/Kingspenguin/ECE143-Project/tree/main/Datasets) Folder.
    ```
    python Data Preparation.py
    ```
2. Then run the 'Dataset Merging For COVID.py' file, which uses the previously created file and 'mortality_data.xlsx' to create 'mortality_merged.csv' file. 
    - This new .csv file created is used for analyzing COVID and mortality rate data in relation to happiness score.
    ```
    python Dataset Merging For COVID.py
    ```
3. Then run the 'COVID data analysis.py', which uses the previously to .csv files we created to make the 'COVID_Analysis_Dataset.csv'.
    - This is the result of doing mathematical analysis on the .csv file and using this to create visualizations.
    ```
    python COVID data analysis.py
    ```
4. Finally, run the [jupyter notebook](https://github.com/Kingspenguin/ECE143-Project/blob/main/notebooks/Visualization%20Final.ipynb) to see all the visualization and graphs created for the project.
    - Warning: The notebook folder contains newplot.png files. The only purpose of those images are to display them on github because fig.show was not displaying some of the graphs on github due to compatibilty issues. If downloaded on desktop all the codes work as intended and it works without the .png files

### File Structure

````sh
.
├── README.md
├── requirements.txt
├── Datasets
├── Python
├── notebooks
```


1. Dataset Folder: Contains all the .csv and .xslx files used for the purpose of the project.
    - Some of the files are downloaded from the links
    - Some of the files were created during data preparation or data merging
2. Python Folder: Contain all the .py files. Some files are solely for the use of data preparations and others are for visualization
    - Data Preparation.py: Creates the 'Happiness_data_from_2015_to_2022.csv' file that we mainly use for analysis and creating visualization.
    - Dataset Merging For COVID.py: Add mortality rates and COVID data to create the 'mortality_merged.csv' file.
    - COVID data analysis.py: Performs mathematical analysis on the 'mortality_merged.csv' file to create the 'COVID_Analysis_Dataset.csv' file.
    - Correlation Matrix Visualization.py: Creates the correlation matrix plot based on the .csv files we created.
3. notebooks Folder: Contains the jupyter notebook with all the visualization used in the presentation.
4. final_presentation: Contains the final presentation slides 

### Third party modules used:

1. [numpy](https://numpy.org/)
2. [pandas](https://pandas.pydata.org/)
3. [matplotlib](https://matplotlib.org/)
4. [seaborn](https://seaborn.pydata.org/)
5. [plotly](https://plotly.com/)
6. [folium](https://python-visualization.github.io/folium/)
7. [geopandas](https://geopandas.org/en/stable/)
8. [sklearn](https://scikit-learn.org/stable/)




