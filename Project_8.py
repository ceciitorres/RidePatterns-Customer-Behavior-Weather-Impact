# Import Libraries
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Import datasets
trips_df = pd.read_csv(r"C:\Users\cecy_\OneDrive\Documentos\Data_Science\Proyectos\Project_Sprint_8\data\moved_project_sql_result_01.csv")
dropoff_df = pd.read_csv(r"C:\Users\cecy_\OneDrive\Documentos\Data_Science\Proyectos\Project_Sprint_8\data\moved_project_sql_result_04.csv")
weather_df = pd.read_csv(r"C:\Users\cecy_\OneDrive\Documentos\Data_Science\Proyectos\Project_Sprint_8\data\moved_project_sql_result_07.csv")

# Check dataframes info
trips_df.info()
trips_df.head(5)
dropoff_df.info()
dropoff_df.head(5)
weather_df.info()
weather_df.head(5)

# Change date column to datetype
weather_df['start_ts'] = pd.to_datetime(weather_df['start_ts'], format='%d/%m/%Y %H:%M', errors='coerce').dt.date
weather_df.info()
weather_df.head(5)
weather_df['start_ts'] = pd.to_datetime(weather_df['start_ts'], format='%d/%m/%Y')
weather_df.info()

# Analyse data from dropoff & trips table
top_10_dropoff_loc = dropoff_df.sort_values(by='average_trips', ascending=False).head(10)
top_10_dropoff_loc['average_trips'] = np.ceil(top_10_dropoff_loc['average_trips']).astype(int)
top_10_dropoff_loc
top_10_cabs_companies = trips_df.sort_values(by='trips_amount', ascending=False).head(10)
top_10_cabs_companies

# Create the Top 10 bar chart Dropoff Locations
locations = top_10_dropoff_loc['dropoff_location_name']
average_trips = top_10_dropoff_loc['average_trips']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(locations, average_trips)
plt.title('Top 10 Drop-off Locations by Average Trips')
plt.xlabel('Drop-off Location')
plt.ylabel('Average Trips')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.show(block=True)

# Create the Top 10 bar chart Cabs Companies
company = top_10_cabs_companies['company_name']
total_trips = top_10_cabs_companies['trips_amount']

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(company, total_trips)
plt.title('Top 10 Drop-off Locations by Average Trips')
plt.xlabel('Drop-off Location')
plt.ylabel('Average Trips')
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()  
plt.show(block=True)

# Conclusion
# The neibourhood where most people is dropoff is Loop with 10,728 average trips,
# follow it by River North and Streeterville with an average of 9,524 and 6,665 respectively
# The most popular company is Flash Cab with a total of 19,558 trips, follow it
# by Taxi Affiliation Services and Medallion Leasin with 11,422 and 10,367 respectively 


