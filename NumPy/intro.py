#To use NumPy with Python, import it at the top of your file using the following line
import numpy as np

# Arrays

test_1 = np.array([92,94,88,91,87])

csv_array = np.genfromtxt('sample.csv', delimiter=',')
#Note that in this case, our file sample.csv has values separated by commas, so we use delimiter=',', but sometimes you’ll find files with other delimiters, 
# the most common being tabs or colons


test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = test_3 + 2


# In order for arrays to be added or subtracted they need to have the same number of elements.
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print (final_grade)

# Two Dimensional Arrays

 # In NumPy we can create an array of arrays. If the arrays that make up our bigger array are all the same size, then it has a special name: 
 # a two-dimensional array

coin_toss = np.array([1,0,0,1,0])

coin_toss_again = np.array([[1,0,0,1,0,], [0,0,1,1,1]])





# Selecting Elements from one dimensional array

# If we wanted to select multiple elements in the array, we can define a range, such as a[1:3],
# which will select all the elements from a[1] to a[3], including a[1] but excluding a[3]
array[1:3]

# Similarly, if we wanted to select all elements before a[3] we would use
a[:3]

# We can also use negative indices to select multiple elements. Let’s say we want to select the last 3 elements in an array

a[-3:]
#Notice that when we select multiple elements, we get an array

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]

manual_adwoa_test_1 = test_1[1:3] #This pulled the two students at indexes 1 and 2 from the test 1 table.




# Selecting Elements from a 2-D Array


#The syntax for selecting from a 2-d array is a[row,column] where a is the array.

#It’s important to note that when we work with arrays that have more than one dimension, the relationship between the interior arrays is defined in terms of
# axes. A two-dimensional array has two axes: axis 0 represents the values that share the same indexical position (are in the same column), 
# and axis 1 represents the values that share an array (are in the same row). This is illustrated below

# Select sepcific element
a[2,1]


# Select entire column
a[:,0]


# Select entire row
>>> a[1,:]

# Select first three elements of the first row

a[0,0:3]

student_scores = np.array([[92, 94, 88, 91, 87],
                        [79, 100, 86, 93, 91],
                        [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2,0]

cody_test_scores = student_scores[:,-1]


# Logical Operators w/Arrays

# Another useful thing that arrays can do is perform element-wise logical operations. For instance, suppose we want to know how many elements in an array
# are greater than 5. We can easily write some code that checks to see whether this statement evaluates to True for each item in the array, 
# without having to use a for loop

>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
>>> a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)

# We can then use logical operators to evaluate and select items based on certain criteria. To select all elements from the previous array 
# that are greater than 5, we’d write the following
a[a > 5]

# We can also combine logical statements to further specify our criteria. To do so, we place each statement in parentheses and use
# boolean operators like & (and) and | (or).
a[(a > 5) | (a < 2)]

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge > 60) & (porridge < 80)]
print (cold, hot, just_right)



temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print(temperatures)

temperatures_fixed = temperatures + 3

print(temperatures_fixed)

monday_temperatures = temperatures_fixed[0,:]

thursday_friday_morning = temperatures_fixed[3:5,1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]