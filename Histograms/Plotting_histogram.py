from matplotlib import pyplot as plt
plt.hist(exercise_ages, range = (20, 70), bins = 5, edgecolor='black')

plt.title("Decade Frequency")
plt.xlabel("Ages")
plt.ylabel("Count")

plt.show()


# Import packages
import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use plt.hist() below
plt.hist(times, range=(0, 24), bins=4,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()



# Same as before but switches bins to 24 so that you have one hour increments instead of six hour blocks.
# Import packages
import codecademylib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values

# Use plt.hist() below
plt.hist(times, range=(0, 24), bins=24,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()