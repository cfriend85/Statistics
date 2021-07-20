#The NumPy library has a function named quantile() that will quickly calculate the quantiles of a dataset for you.
#quantile() takes two parameters. The first is the dataset that you are using. The second parameter is a single number or a list of numbers between 0 and 1. 
#These numbers represent the places in the data where you want to split.
#For example, if you only wanted the value that split the first 10% of the data apart from the remaining 90%, you could use this code:

import numpy as np

dataset = [5, 10, -20, 42, -9, 10]
ten_percent = np.quantile(dataset, 0.10)

from song_data import songs
import numpy as np

# Define twenty_third_percentile here:
twenty_third_percentile = np.quantile(songs, 0.23)

try:
    print("The value that splits 23% of the data is " + str(twenty_third_percentile) + "\n")
except NameError:
    print("You haven't defined twenty_third_percentile.")


#  quantiles are usually a set of values that split the data into groups of equal size. For example, you wanted to get the 5-quantiles, 
# or the four values that split the data into five groups of equal size, you could use this code:

import numpy as np

dataset = [5, 10, -20, 42, -9, 10]
ten_percent = np.quantile(dataset, [0.2, 0.4, 0.6, 0.8])






from song_data import songs
import numpy as np

# Define quartiles, deciles, and tenth here:
quartiles = np.quantile(songs, [0.25, 0.5, 0.75])
deciles = np.quantile(songs, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
tenth = 3

try:
    print("The quariles are " + str(quartiles) + "\n")
except NameError:
    print("You haven't defined quartiles.\n")
try:
    print("The deciles are " + str(deciles) + "\n")
except NameError:
    print("You haven't defined deciles.\n")


from song_data import songs
import numpy as np

# Define percentile and answer here:
percentile = np.quantile(songs, 0.32)
answer = "below"

try:
    print("Your percentile is " + str(percentile) + "\n")
except NameError:
    print("You haven't defined percentile")


# Interquartile Range

#The interquartile range (IQR) is a descriptive statistic that tries to solve the problem of outliers. 
# The IQR ignores the tails of the dataset, so you know the range around-which your data is centered.

from song_data import songs
import matplotlib.pyplot as plt

maximum = max(songs)
minimum = min(songs)
#Create the variable song_range here:
song_range = maximum - minimum

# Ignore the code below here
plt.hist(songs, bins = 200)
plt.xlabel("Song Length (Seconds)")
plt.ylabel("Count")
plt.show()

try:
    print("The range of the dataset is " + str(song_range) + " seconds")
except NameError:
    print("You haven't defined the variable song_range yet")

#the first quartile is the value that separates the first 25% of the data from the remaining 75%.
# The third quartile is the opposite — it separates the first 75% of the data from the remaining 25%
#The interquartile range is the difference between these two values:
# IQR = Q3-Q1


from song_data import songs
import numpy as np

q1 = np.quantile(songs, 0.25)
#Create the variables q3 and interquartile_range here:
q3 = np.quantile(songs, 0.75)
interquartile_range = q3 - q1


from song_data import songs
from scipy.stats import iqr

#Create the variables interquartile_range here:
interquartile_range = iqr(songs)
#The iqr() function takes a dataset as a parameter and returns the Interquartile Range.
#  Notice that when we imported iqr(), we imported it from the stats submodule