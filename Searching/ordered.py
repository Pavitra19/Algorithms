# Searching for an item in an ordered list
# This technique uses a binary search
# O(log n)

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binarysearch(item, item_list):
    # Get the list size
    list_size = len(item_list) - 1
    # Start at the two ends of the list
    lower_index = 0
    upper_index = list_size

    while lower_index <= upper_index:
        # Calculate the midpoint
        # Round down
        midpoint = (lower_index + upper_index) // 2

        # If the item is found, return the index
        if item_list[midpoint] == item:
            return midpoint

        # Otherwise get the next midpoint
        # If the item is larger than the value at the midpoint,
        # Move the lower index to be above midpoint
        if item > item_list[midpoint]:
            lower_index = midpoint + 1
        else:
            upper_index = midpoint - 1

    if lower_index > upper_index:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
