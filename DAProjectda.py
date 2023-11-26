import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
file_path = './data/Annual_Surface_Temperature_Change.csv'
surface_temp_data = pd.read_csv(file_path)

# Define the years column outside of the South Korea conditional block
years = surface_temp_data.columns[10:]  # Adjust this to match the structure of your CSV

# Check and extract data for South Korea
if 'Korea, Rep. of' in surface_temp_data['Country'].values:
    south_korea_data = surface_temp_data[surface_temp_data['Country'] == 'Korea, Rep. of']
    if not south_korea_data.empty:
        temperatures = south_korea_data.iloc[0][years]

        # Plot and save the first graph
        plt.figure(figsize=(15, 6))
        plt.plot(years, temperatures, marker='o', linestyle='-')
        plt.title('Yearly Surface Temperature Change in South Korea (1960-2022)')
        plt.xlabel('Year')
        plt.ylabel('Temperature Change (°C)')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.savefig('./graphs/south_korea_temp_change.png')
else:
    print("South Korea data not found.")

# Rest of your code for other graphs...

# Calculate and plot global average temperatures
global_avg_temperatures = surface_temp_data[years].mean()

# Plot and save the third graph
plt.figure(figsize=(15, 6))
plt.plot(years, global_avg_temperatures, marker='o', linestyle='-', color='green')
plt.title('Global Average Yearly Surface Temperature Change (1960-2022)')
plt.xlabel('Year')
plt.ylabel('Average Temperature Change (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('./graphs/global_avg_temp_change.png')
