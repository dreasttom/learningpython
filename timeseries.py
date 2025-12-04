import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate random time-series data
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', periods=100, freq='D')
values = np.random.randn(100).cumsum()

# Create a DataFrame from the generated data
data = pd.DataFrame({'date': dates, 'value': values})

# Set the 'date' column as the index
data.set_index('date', inplace=True)

# Plot the time-series data
plt.plot(data.index, data['value'])
plt.xlabel('Time')
plt.ylabel('Value')
plt.xticks(rotation = 45)
plt.title('Time Series Data')
plt.show()
