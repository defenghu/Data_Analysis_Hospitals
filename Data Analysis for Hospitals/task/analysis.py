# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV files into pandas DataFrames
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

# Set pandas option to display all columns for better visibility
pd.set_option('display.max_columns', None)

# Standardize column names across all DataFrames for consistency
prenatal.columns = general.columns
sports.columns = general.columns

# Combine all DataFrames into a single DataFrame
df = pd.concat([general, prenatal, sports], ignore_index=True)

# Remove unnecessary columns and rows with excessive missing values
df.drop(columns='Unnamed: 0', inplace=True)
df.dropna(axis='rows', inplace=True, thresh=3)

# Standardize gender values to 'm' for male and 'f' for female
df.loc[(df['gender'] == 'male') | (df['gender'] == 'man'), 'gender'] = 'm'
df.loc[(df['gender'] == 'female') | (df['gender'] == 'woman'), 'gender'] = 'f'

# Fill missing values in the 'bmi' to 'months' columns with 0 and 'f' for gender
df.loc[:, 'bmi':'months'] = df.loc[:, 'bmi':'months'].fillna(0)
df['gender'].fillna('f', inplace=True)


# Function to calculate the proportion of patients with a specific diagnosis in a specific hospital
def calculate_share(df, hospital, diagnosis):
    # Count the number of patients with the specified diagnosis in the specified hospital
    patients_with_diagnosis = df[(df['hospital'] == hospital) & (df['diagnosis'] == diagnosis)].shape[0]
    # Count the total number of patients in the specified hospital
    total_patients = df[df['hospital'] == hospital].shape[0]
    # Calculate and return the proportion of patients with the specified diagnosis
    share = round(patients_with_diagnosis / total_patients, 3)
    return share


# Calculate required statistics
one = df.groupby('hospital').size().sort_values(ascending=False).index[0]
two = calculate_share(df, 'general', 'stomach')
three = calculate_share(df, 'sports', 'dislocation')
median_general = df[df['hospital'] == 'general']['age'].median()
median_sports = df[df['hospital'] == 'sports']['age'].median()
four = abs(median_general - median_sports)

# Create a pivot table to count the number of blood tests taken in each hospital
table = pd.pivot_table(df, values='age', index='hospital', columns='blood_test', aggfunc='count')
most_blood_tests = table['t'].idxmax()
num_tests = table['t'].max()

# Print the results
# print(f"The answer to the 1st question: {one}\n"
#       f"The answer to the 2nd question: {two}\n"
#       f"The answer to the 3rd question: {three}\n"
#       f"The answer to the 4th question: {four}\n"
#       f"The answer to the 5th question: {most_blood_tests}, {num_tests} blood tests")

# Define age ranges and categorize patient ages into these ranges
bins = [0, 15, 35, 55, 70, 80]
df['age_range'] = pd.cut(df['age'], bins)

# Find the most common age range among patients
most_common_age_range = df['age_range'].value_counts().idxmax()
# Format the age range string for cleaner output
age_range_formatted = str(most_common_age_range).replace('(', '').replace(']', '').replace(',', '-').replace(' ', '')

# Plot a histogram of patient ages
plt.hist(df['age'], bins=bins, edgecolor='white')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.title('Distribution of Patient Age')
plt.show()

# Count the number of occurrences of each diagnosis
diagnosis_counts = df['diagnosis'].value_counts()

# Create a pie chart of diagnosis counts
plt.figure(figsize=(10, 7))
plt.pie(diagnosis_counts, labels=diagnosis_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Most Common Diagnosis Among Patients')
plt.show()

# Convert height values from feet to meters for patients in the 'sports' hospital
conversion_factor = 0.3048
df.loc[df['hospital'] == 'sports', 'height'] = df.loc[df['hospital'] == 'sports', 'height'] * conversion_factor

# Create a violin plot of patient height distribution by hospital
sns.violinplot(x='hospital', y='height', data=df)
plt.title('Height Distribution by Hospital')
plt.xlabel('Hospital')
plt.ylabel('Height')
plt.show()

# Explanation for the gap in height values and the two peaks in the violin plot
answer = "The gap in values and the two peaks are due to the height in the sports hospital being given in feet instead of meters."

# Print the answers to the questions
print(f"The answer to the 1st question: {age_range_formatted}\n"
      f"The answer to the 2nd question: {diagnosis_counts.idxmax()}\n"
      f"The answer to the 3rd question: {answer}\n")
