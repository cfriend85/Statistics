import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = grades[0] - mean
difference_two = grades[1] - mean
difference_three = grades[2] - mean
difference_four = grades[3] - mean
difference_five = grades[4] - mean


print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")



# Avg distances
import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = 88 - mean
difference_two = 82 - mean
difference_three = 85 - mean
difference_four = 84 - mean
difference_five = 90 - mean

#Part 1: Sum the differences
difference_sum = difference_one + difference_two + difference_three + difference_four + difference_five

#Part 2: Average the differences
average_difference = difference_sum / 5

print("The sum of the differences is " + str(format(difference_sum, "f")))
print("The average difference is " + str(format(average_difference, "f")))