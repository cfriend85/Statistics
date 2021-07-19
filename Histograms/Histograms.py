# The purpose of a histogram is to summarize data that you can use to inform a decision or explain a distribution
# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Print transactions below
print(transactions)
print(np.average(times))

min_age = np.amin(exercise_ages) # check the min value of an array
max_age = np.amax(exercise_ages) # check the max value of an array
age_range = max_age - min_age #find the range


# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction data to numpy arrays
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Find the minimum time, maximum time, and range

min_time = np.amin(times) #min of array
max_time = np.amax(times) #max of array
range_time = max_time - min_time #range of array

# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))



# A bin is a sub-range of values that falls within the range of a dataset. In the grocery store example, a valid bin may be from 0 hours to 6 hours. 

# This bin includes all times from just after midnight (0) until 6 am (6).

# Additionally, all bins in a histogram must be the same width.

#If the range of values in our dataset is from 0 to 24, and the first bin in our grocery store example is from 0 to 6

# The grocery store bins are: 0 to 6 hours, 6 to 12 hours, 12 to 18 hours, 18 to 24 hours

# Import packages
import numpy as np
import pandas as pd

# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])

# Set the minimum and maximums of the array below
min_days_old = np.amin(days_old_bread)
max_days_old = np.amax(days_old_bread)

# Set the number of bins to 3
bins = 3

# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")

# OUTPUT: Bins: 3, Bin Width: 3.0


# Import packages
import numpy as np
import pandas as pd

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use numpy.histogram() below
times_hist = np.histogram(times, range = (0, 24), bins = 4)

print(times_hist)

#OUTPUT: (array([101, 231, 213, 455]), array([ 0.,  6., 12., 18., 24.])) first array is a count of how many in each bin, second is the ranges of each bin.
#In this case the last bin - hours 6-12 are the busiest times for the store.

#Example explanation of distribution of a dataset:

#This histogram displays the distribution of chest pain cost for over 2,000 hospitals across the United States. The average and median costs are $16,948 
# and $14,659.6, respectively. Given that the data is unimodal, with one local maximum and a right skew, 
# the fact that the average is greater than the median, matches our expectation.
# #The range of costs is very large, $78,623, with the smallest cost equal to $2,459 and the largest cost equal to $81,083.
# There is one hospital, Bayonne Hospital Center, that charges far more than the rest at $81,083.


#Nice work, the long tail to the right of the distribution indicates that it is skewed to the right, 
# and will make the mean greater than the median of the distribution.
