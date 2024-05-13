# Example of load multiple datasets end with .csv under the same directory
# In this example, I used the NBA games data from Kaggle 
# (https://www.kaggle.com/datasets/nathanlauga/nba-games)

# import numpy as np
import pandas as pd
from pyprojroot.here import here

# Load multiple datasets end with .csv under the same directory 
# and assign names based on the file names
def load_data(data_path):
    data = {} # Create an empty dictionary to store data
    data_path = data_path # Get the path of the data directory
    for file in data_path.glob("*.csv"):
        data[file.stem] = pd.read_csv(file) # Read data and assign names
    return data
  
# Load data
data = load_data(here("data/raw"))

# Print the keys of the dictionary
print(data.keys())

# Print the first 5 rows of the first dataset
print(data["teams"].head())


