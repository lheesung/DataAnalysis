import pandas as pd
import matplotlib.pyplot as plt

file_path = './data/Annual_Surface_Temperature_Change.csv'
surface_temp_data = pd.read_csv(file_path)

# Extract data for South Korea
south_korea_data = surface_temp_data[surface_temp_data['Country'] == 'Korea, Rep. of']
years = south_korea_data.columns[10:]
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

# Extract and plot data for selected countries
selected_countries = ['United States of America', 'China', 'India', 'Brazil', 'Korea, Rep. of', 'Germany']
comparison_data = surface_temp_data[surface_temp_data['Country'].isin(selected_countries)]
latest_year = 'F2022'
latest_temperatures = comparison_data[['Country', latest_year]]

# Plot and save the second graph
plt.figure(figsize=(12, 6))
plt.bar(latest_temperatures['Country'], latest_temperatures[latest_year], color='skyblue')
plt.title(f'Temperature Change in {latest_year} - Comparison among Selected Countries')
plt.xlabel('Country')
plt.ylabel(f'Temperature Change in {latest_year} (°C)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.savefig('./graphs/comparison_selected_countries.png')

# Calculate and plot global average temperatures
import numpy as np
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
