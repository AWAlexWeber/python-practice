# This is an exploration of the basics of the fundamental array structure within python
# An array in pyhton, unlike most languages, is functionally the same thing as a list (or dynamic array)

# Defining a couple of arrays through a variety of methods
array = [1,2,3,4,5,6,7,8,9]
array_empty = []
array_just_zeros = [0] * 10

# Appending 
array.append(15)

# Adding multiple objects via extend
# This is effectively append but O(n) times
array.extend([1,2,3,4,5,6,7,8,9,10])

# We can actually perform basic math on arrays (if we use numpy)
#import numpy as np
#print(np(array)*np(array))

# Clearing the array
array.clear()

# Array comparator
if (array == array_empty):
    # We cleared it!
    print("Array is now empty")

# Creates a new copy
array_two = array.copy()
array_three = array

array.append(1)

# In this case array_two is empty but array_three and array are not (since they are the same array!)
# Index helps us find certain values
array.extend([2,3,4,5,6,7,8,9])
array[array.index(3)] = 0

# Pop will delete an element entirely
# Note that this is O(n)! 
array.pop(3)

# Remove will delete a specific value 
array.remove(5)

# Now we can reverse it
# Note that this function does not need to be caught, it reverses itself
array.reverse()

# Also allow sorting
array.sort()

### Complexity ###
# Copy: O(n)
# Append(1): O(1)
# Pop Last: O(1)
# Pop Intermediate: O(k) where K is the number of elements afterwards
# Insert: O(n) where N is the number of elements
# Get/Set: O(1)
# Delete: O(n) where N is the number of elements after the element
# Iteration: O(n)
# Extent: O(k) where K is number of elements being appended

# See more here: https://wiki.python.org/moin/TimeComplexity