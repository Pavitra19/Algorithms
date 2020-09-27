# Determine if a list is sorted

items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted1(item_list):
    # Method 1, using brute force
    for i in range(0, len(item_list) - 1):
        if item_list[i] > item_list[i+1]:
            return False

    return True


def is_sorted2(item_list):
    # Method 2
    # All function has a boolean result
    return all(item_list[i] <= item_list[i+1] for i in range(len(item_list)-1))


print(is_sorted1(items1))
print(is_sorted1(items2))
print(is_sorted2(items1))
print(is_sorted2(items2))
