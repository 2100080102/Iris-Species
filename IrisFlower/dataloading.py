import pandas as pd

# Load dataset
df = pd.read_csv('D:\\Users\\acer\\PycharmProjects\\DataScience\\IrisFlower\\IRIS.csv')

# Display the first few rows of the dataset
print(df.head())

# Display basic information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Basic statistics of the dataset
print(df.describe())
