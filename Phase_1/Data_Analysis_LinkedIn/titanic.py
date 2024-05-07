import pandas as pd
import numpy as np

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Display the first few rows
# print(df.head)

# View the data types and summary information
# print(df.info)

# Get statiscaal summary of the dataset
# print(df.describe())

# Clean data
# df.dropna(subset=['Age'], inplace=True)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Countplot of Survived passengers
# sns.countplot(x = 'Survived', data=df)
# plt.title('Survival Count')

# Histogram of Age Distribution
# plt.hist(df['Age'], bins = 20)
# plt.xlabel('Age')
# plt.ylabel('Count')
# plt.title('Age Distribution')
# plt.show()

# Boxplot of Fare with respect to Survival
# sns.boxplot(x = 'Survived', y = 'Fare', data = df)
# plt.title('Fare Distribution by Survival')
# plt.show()

# Boxplot of Age with respect to Survival
# sns.boxplot(x = 'Survived', y = 'Age', data = df)
# plt.title('Age Distribution by Survival')
# plt.show()

# Data Analysis and Calculations
#  Calculate the mean age
mean_age = np.mean(df['Age'])
# print(mean_age)

# Calculate the standard deviation of age
std_age = np.std(df['Age'])
# print(std_age)

# Calculate the the correlation between age and Fare
correlation_matrix = np.corrcoef(df['Age'], df['Fare'])
print(correlation_matrix)