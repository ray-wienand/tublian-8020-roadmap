import pandas as pd
import sys

# ***** ----- SOME EXAMPLES FOR NON JUPYTER FILES ----- *****


# print(sys.version)
# print('pandas version', pd.__version__)

df = pd.read_parquet("Combined_Flights_2022.parquet")

# ***** --- READING AND WRITING --- *****

# print(type(df)) # Print df type
# df.to_csv('Combined_Flights_2022.csv')
# pd.set_option("display.max_columns", 500) # Overrides the number of columns
# print(df.head()) # Default print 1st 5 rows
# print(df.head(3)) # Overrides default 5 rows
# print(df.tail()) # Prints the last 5 rows
# print(df.tail(10)) # Overrides the default last 5 rows
# print(df.sample(5)) # Prints 5 random rows
# print(df.sample(frac=0.1)) # Print a fraction % sample of the dataset
# print(df.sample(frac=0.1, random_state=529)) # Print a fraction % sample of the dataset
# print(df.columns) #Prints all the column headers
# print(df.index) # Prints all the index values
# print(df.info()) # Prints info about the df
# print(df.info(verbose = False)) # Prints a quicker info about the df
# print(df.describe()) # Prints a description for all numerical columns
# print(df[['Airline']].describe()) # Prints a description for all non-numerical columns
# print(df.shape) # Prints the number of rows & columns
# print(df.shape, len(df)) # Prints the shape and the number of rows

# ***** --- SUBSETTING A DATAFRAME --- ****
# --- Subsetting columns and rows ---
#  - Subsetting columns -

# print(df[['FlightDate', 'Airline', 'Origin']]) # Creates and prints a subset that only contains the specified columns
# fao = df[['FlightDate', 'Airline', 'Origin']] # Create a new dataset
# print(fao)
# print(df.columns[:5]) # Slices and prints the first 5 columns
# print(df.columns[-5:]) # Slices and prints the last 5 columns
# print([c for c in df.columns if 'Time' in c]) # Filters down and Prints only the columns where there is time in the heading
# print(df.select_dtypes('int')) # Filters and prints only the columns that has the dtype of int
# airline = df['Airline'] # Creates a subset with the series of the Airlines columns
# print(airline)
# airline = df[['Airline']] # Creates a subset dataframe with the series of the Airlines columns
# print(airline)

# - Subseting rows
# Allows you to access elements in relation to their location in the df
# df.loc[] - Uses the names
# df.iloc[] - Uses the index value
# print(df.iloc[1, 3]) # Prints the value of row 3, column 5
# print(df.iloc[:5, :5]) # Slices the 1st 5 rows and olumns
# print(df.iloc[[5]]) # Filters the 1st 5 rows
# print(df.iloc[:, 1]) # Slices it to 1 column
# print(df.iloc[:, [1, 2]]) # Puts it in a new df with the 1st two columns.
# print(df.loc[:, ['Airline', 'Origin']]) # Uses the column names instead of the numbers
# print(df['Airline'] == 'Spirit Air Lines') #  Creates a series of true and false. 
# print(df.loc[(df['Airline'] == 'Spirit Air Lines') & (df['FlightDate'] == '2022-03-30')]) #  Filters it down to a spesific column and date 
# print(df.loc[~((df['Airline'] == 'Spirit Air Lines') & (df['FlightDate'] == '2022-03-30'))]) #  ~ Excludes the columns 
