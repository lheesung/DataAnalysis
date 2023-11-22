import pandas as pd

# Load the CSV file
file_path = './data/Annual_Surface_Temperature_Change.csv'
surface_temp_data = pd.read_csv(file_path)

surface_temp_data.head()