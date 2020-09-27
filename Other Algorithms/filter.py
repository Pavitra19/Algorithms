# Use a hashtable/dictionary to filter out duplication items
# O(n)

# Define a set of items that we want to reduce duplications
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# Create a dictionary to perform a filter
filter = dict()

# Loop over each item and add to the dictionary
for key in items:
    filter[key] = 0
print(filter)

# Create a set from the resulting keys in the dictionary
result = set(filter.keys())
print(result)
