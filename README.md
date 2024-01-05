# Hospital Data Analysis
This is the Data Analysis for Hospitals project I made myself.

You know the story. Data is everywhere: texts, images, news, and spreadsheets. It affects our habits and defines our future. The amount of data is growing by the second. How can one stay afloat in this great sea of data? Data analysis is required in any line of business. In this project, you will conduct a comprehensive study with pandas. You will upload datasets, deal with data omissions and incorrect data filling, find the main statistical characteristics, and visualize your data. Let's do it!

This project involves the analysis of data from three different hospitals: General, Prenatal, and Sports. The data includes information about patients' age, gender, diagnosis, and various medical tests. The goal of this project is to extract meaningful insights from the data and answer specific questions related to patient demographics, diagnoses, and medical tests.

# Data Preparation
The data is read from three separate CSV files, one for each hospital. The column names are standardized across all dataframes for consistency. The dataframes are then concatenated into one for ease of analysis.
Unnecessary columns are dropped, and rows with too many missing values are removed. The gender values are standardized to 'm' for male and 'f' for female. Missing values in certain columns are filled with 0, and missing gender values are filled with 'f'.
# Analysis
- The analysis involves calculating various statistics and creating visualizations to answer specific questions. These include:
- The hospital with the most patients.
- The share of patients with a specific diagnosis in a specific hospital.
- The difference in median age of patients between two hospitals.
- The hospital with the most blood tests.
- The results are printed to the console.
# Visualizations
Histograms, pie charts, and violin plots are created to visualize the data. These visualizations help answer questions about the most common age range among all patients, the most common diagnosis, and the distribution of patient height by hospital.
## Built With
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
