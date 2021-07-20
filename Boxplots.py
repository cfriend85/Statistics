#Boxplots are one of the most common ways to visualize a dataset. Like histograms,
#boxplots give you a sense of the central tendency and spread of the data.
#The line in the center of the box is the median.
#The edges of the box are the first and third quartiles. This makes the length of the box the interquartile range — the middle 50% of your data.
#The whiskers of the boxplot extend to include most of the data. There are many different ways to calculate the length of the whiskers.
#Outliers are points that fall beyond the whiskers. Those points are represented with dots. In the boxplot we’re showing, there are many outliers

import numpy as np
from data import dataset

# Define dataset_median here:
dataset_median = np.median(dataset)

# Define quartile_one and quartile_three here:
quartile_one = np.quantile(dataset, 0.25)
quartile_three = np.quantile(dataset, 0.75)


# Set up whiskers
iqr = quartile_three - quartile_one
distance = iqr * 1.5
left_whisker = quartile_one - distance
right_whisker = quartile_three + distance


# Boxplots in Matplotlib

import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two

plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels=["2000 Songs", "2001 Songs", "2002 Songs"])
plt.show()