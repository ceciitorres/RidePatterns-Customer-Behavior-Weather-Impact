# Import Libraries
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as st


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
# Los vecindarios donde la mayotia de los viajes son finalizado es Loop con una media de 10,728 vaijes,
# seguido por River North y Streeterville con una media de 9,524 y 6,665 respectivamente

# The most popular company is Flash Cab with a total of 19,558 trips, follow it
# by Taxi Affiliation Services and Medallion Leasin with 11,422 and 10,367 respectively 
# La compañia mas popular es Flash Cab con un total de 19,558 viajes, seguida por
# Taxi Affiliation Services y Medallion Leasin con 11,442 y 10,367 respectivamente.


# Prove the hypothesis 
# "Average trip length from the Loop to O'Hare International Airport changes on rainy Saturdays."
# "La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos".


# Visualised the DataFrame
weather_df.head(10)

# Compare days
rainy_days = weather_df[weather_df['weather_conditions'] == 'Bad']
other_days = weather_df[weather_df['weather_conditions'] == 'Good']

# Caculate average trip duration
rainy_days_avg = rainy_days['duration_seconds'].mean()
other_days_avg = other_days['duration_seconds'].mean()
print(f"Average Duration on Rainy Saturdays: {rainy_days_avg} seconds")
print(f"Average Duration on Non-Rainy Saturdays: {other_days_avg} seconds")

# Perform a two-sample t-test
t_stat, p_value = st.ttest_ind(
    rainy_days['duration_seconds'],
    other_days['duration_seconds'],
    equal_var=False  # Assume unequal variance
)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Conclusion
if p_value < 0.05:
    print("The average trip duration significantly changes on rainy Saturdays.")
else:
    print("No significant difference in average trip duration on rainy Saturdays.")
    
# Hypothesis and Conclusion
# A two-tailed test was used since with this we can consider two possibilities, 
# that the duration is the same or different.
# For the null hypothesis, it is considered that the average duration of trips on rainy 
# days is the same or significantly similar to the rest of the days, therefore the 
# alternative hypothesis suggests that the duration of trips on Saturdays without rain 
# are significantly different from rainy days

# Hipotesis ay Conclusion
# Se utilizó una prueba de dos colas ya que con esta podemos considerar dos posibilidades, 
# que la duración sea igual o distinta.
# Para la hipotesis nula se considera que la media de duracion de los viajes los dias 
# lluviosos es igual o significativamente similar a el resto de los dias, por lo tanto 
# la hipotesis alternativa sugiere que la duracion de los viajes los Sabados sin lluvia 
# son significativamente diferentes a los dias de lluvis