#Data Analysis and Visualization
#Description: Analyze COVID-19 cases worldwide and visualize trends over time using Python libraries like Pandas and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('covid19_data.csv')

# Filter data for a specific country
country_data = data[data['Country'] == 'India']

# Plot cases over time
plt.plot(country_data['Date'], country_data['Cases'], label='COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Cases Over Time')
plt.legend()
plt.show()
