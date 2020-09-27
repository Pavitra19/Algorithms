# Use a dictionary to count individual items
# O(n)

# Define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# Create a dictionary object to hold the items and counts
counter = dict()

# Iterate over each item and increment the count for each one
for item in items:
    if(item in counter.keys()):
        # If item already exists in set of keys, increment value
        counter[item] += 1
    else:
        # Initialize key's value
        counter[item] = 1

# Print the results
print(counter)
