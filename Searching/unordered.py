# Searching for an item in an unordered list
# Sometimes called a Linear search
# Time complexity: O(n)

# Declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(item, item_list):
    for i in range(0, len(items)):
        if item == item_list[i]:
            return i  # Return position if in list

    # Not in list
    return None


print(find_item(87, items))  # In list
print(find_item(250, items))  # Not in list
