# Bring panda data analytics library into environment
import pandas as pd

# Read in data from excel sheet
data = pd.read_csv("C:\\Users\gavin\OneDrive\Documents\iris_csv.csv")

# Read off data in Python
data.head()

# Display a random number of rows
data.sample(10)

# Display columns and column names
data.columns()

# Display the number of row and column entries
data.shape()

# Print out the whole dataset in its entirety
print(data)

# Slice the rows you wish to print pr edit
print(data[8:16]) # This prints rows 8 -16

# Save in a variable for further use in analysis of data
sliceOfData = data[8:16]
print(sliceOfData)

# Display and Save only certain columns
specific_data = data[["Id", "Species"]]
print(specific_data.head(10)) # Print first 10 columns of this specific data

# Filtering rows using iloc and loc functions
data.iloc[5]
data.loc[data["Species"] == "Iris-setosa"] # Display only records with Iris-setosa

# Counting unique variables
data["Species"].value_counts() # Displays in descending order

# Calculate mean, mode and sum of a column
sum_data = data["SepalLengthCm"].sum()
mean_data = data["SepalLengthCm"].mean()
median_data = data["SepalLengthCm"].mode()

print("Sum: ", sum_data, "\nMean: ", mean_data, "\nMedian: ", median_data)

# Extract minimum and maximum values from a column
min_data = data["SepalLengthCm"].min()
max_data = data["SepalLengthCm"].max()

print("Minimum: ", min_data, "\nMaximum: ", max_data)

# Add a column to the dataset
cols = data.columns # Assign a varibale to the columns
print(cols) # Print the total list
cols = cols[1:5] # Take the columns with integer values
data1 = data[cols] # Save in a new dataframe
data["total_values"] = data1[cols].sum(axis=1) # Add new column "total_values" to the dataframe
# Use axis 1 to work within rows, axis 0 for columns

# Rename a column
newcols = {
    "Id":"id",
    "SepalLengthCm":"sepallength",
    "SepalWidthCm":"sepalwidth"}

data.rename(columns = newcols, inplace = True)

print(data.head())

# Render a datagram
data.style()

# If you wish to highlight certain key rows...
data.head(10).style.highlight_max(color = 'lightgreen', axis = 0)
data.head(10).style.highlight_max(color = 'lightgreen', axis = 1)
data.head(10).style.highlight_max(color = 'lightgreen', axis = None)

# Clean and Detect Null Values
data.isNull() # If data is missing, it will display true or false
data.isNull.sum() # Display how many null values per column

# How to Heatmap Data using Seaborn
import seaborn as sns
iris = sns.load_dataset("iris")
sns.heatmap(iris.corr(), camp = "YlGnBu", linecolor = "white", linewidths = 1, annot = True) # Annotate each cell with numeric value with annot

# Dataframe Correlation
data.corr(method = 'pearson')

# Multivariate Analysis
g = sns.pairplot(data, hue = "Species") # Pairplot used to Visualise relationships between column variables