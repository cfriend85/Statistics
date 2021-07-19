# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins=365)
plt.title('Flights by Day')
plt.xlabel('Day of the year')
plt.ylabel('Number of flights')

plt.subplot(212)
plt.hist(in_bloom, range=(0, 365), bins=365)
plt.title('Blooms by Day')
plt.ylabel('Number of blooming flowers')
plt.tight_layout()
plt.show()

# This creates two graphs that don't overlap showing the data they're based on by the same parameters.