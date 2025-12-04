import matplotlib.pyplot as plt
import numpy as np

# --- Bar Chart Demonstration ---

# Data for the bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 55]

# Create the bar chart
plt.figure(figsize=(8, 6)) # Set the figure size
plt.bar(categories, values, color='skyblue') # Create the bar plot

# Add titles and labels
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Sample Bar Chart')

# Display the bar chart
plt.show()

# --- Pie Chart Demonstration ---

# Data for the pie chart
labels = ['Apple', 'Banana', 'Orange', 'Grape']
sizes = [15, 30, 45, 10] # Proportions for each slice
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'] # Colors for each slice
explode = (0, 0.1, 0, 0)  # 'explode' a slice (e.g., Banana) to emphasize it

# Create the pie chart
plt.figure(figsize=(8, 8)) # Set the figure size (equal for a perfect circle)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140) # Create the pie plot

# Add a title and ensure the circle is drawn proportionally
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Sample Pie Chart')

# Display the pie chart
plt.show()
