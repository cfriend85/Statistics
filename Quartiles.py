#A common way to communicate a high-level overview of a dataset is to find the values that split the data into four groups of equal size.
#By doing this, we can then say whether a new datapoint falls in the first, second, third, or fourth quarter of the data
#The values that split the data into fourths are the quartiles

from song_data import songs
import matplotlib.pyplot as plt

# plt.hist(songs, bins = 200)
# plt.axvline(x=364, label="Chicago", c = 'r')
# plt.xlabel("Song Length (Seconds)")
# plt.ylabel("Count")
# plt.legend()
# plt.show()


dataset_one = [50, 10, 4, -3, 4, -20, 2] 
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two = [24, 20, 1, 45, -15, 40]
# sorted dataset_two [-15, 1, 20, 24, 40, 45] -CF
#Define the second quartile of both datasets here:
dataset_one_q2 = 4 #BC 4 is in the middle there are an even number of values on either side
dataset_two_q2 = 22 #BC there are not even numbers on either side you take the two in the middle and find thier avg.
#Ignore the code below here:
try:
    print("The second quartile of dataset one is " + str(dataset_one_q2))
except NameError:
    print("You haven't defined dataset_one_q2")
try:
    print("The second quartile of dataset two is " + str(dataset_two_q2))
except NameError:
    print("You haven't defined dataset_two_q2")




dataset_one = [50, 10, 4, -3, 4, -20, 2]
#Sorted dataset_one: [-20, -3, 2, 4, 4, 10, 50]

dataset_two = [24, 20, 1, 45, -15, 40]

dataset_one_q2 = 4
dataset_two_q2 = 22
#Define the first and third quartile of both datasets here: Find the median value on each side of the second quartile.
dataset_one_q1 = -3 
dataset_one_q3 = 10
dataset_two_q1 = 1
dataset_two_q3 = 40


# Quantile
import numpy as np

dataset = [50, 10, 4, -3, 4, -20, 2]
third_quartile = np.quantile(dataset, 0.75)
#The quantile() function takes two parameters. The first is the dataset you’re interested in. The second is a number between 0 and 1.
#Since we calculated the third quartile, we used 0.75 — we want the point that splits the first 75% of the data from the rest.
#For the second quartile, we’d use 0.5. This will give you the point that 50% of the data is below and 50% is above.

from song_data import songs
import numpy as np

#Create the variables songs_q1, songs_q2, and songs_q3 here:
songs_q1 = np.quantile(songs, 0.25)
songs_q2 = np.quantile(songs, 0.50)
songs_q3 = np.quantile(songs, 0.75)
favorite_song = 257
quarter = 2
try:
    print("The first quartile of dataset one is " + str(songs_q1) + " seconds")
except NameError:
    print("You haven't defined songs_q1")
try:
    print("The second quartile of dataset one is " + str(songs_q2)+ " seconds")
except NameError:
    print("You haven't defined songs_q2")
try:
    print("The third quartile of dataset one is " + str(songs_q3)+ " seconds")
except NameError:
    print("You haven't defined songs_q3\n")