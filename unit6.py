import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Define variables
hours = [6, 9, 12, 12, 15, 21, 24, 24, 27, 30, 36, 39, 45, 48, 57, 60]
happ = [12, 18, 30, 42, 48, 78, 90, 96, 96, 90, 84, 78, 66, 54, 36, 24]

# Create scatter plot
plt.scatter(hours, happi)
plt.xlabel('Hours')
plt.ylabel('Happiness')
plt.title('Scatter Plot of Hours vs Happiness')
plt.grid(True)
plt.show()

# Polynomial fit with degree = 2
model = np.poly1d(np.polyfit(hours, happ, 2))

# Add fitted polynomial line to scatter plot
polyline = np.linspace(1, 60, 50)
plt.scatter(hours, happ)
plt.plot(polYline, model(polYline))
plt.xlabel('Hours')
plt.ylabel('Happiness')
plt.title('Polynomial Fit (Degree = 2) of Hours vs Happiness')
plt.grid(True)
plt.show()

# Define function to calculate r-squared
def polyfit(x, y, degree):
  results = {}
  coeffs = np.polyfit(x, y, degree)
  p = np.poly1d(coeffs)
  # Calculate r-squared
  yhat = p(x)
  ybar = np.sum(y)/len(y)
  ssreg = np.sum((yhat-ybar**2)
  sstot = np.sum((y - ybar)**2)
  results['r_squared'] = ssreg / sstot
  return results

# Find r-squared of polynomial model with degree = 2
print(polyfit(hours, happ, 2))
print(polyfit(hours, happ, 2))