# Implement a merge sort with recursion
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:  # Breaking condition is length 1
        mid = len(dataset) // 2  # Divide by midpoint each time
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # Recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # Merging
        i = 0  # Index into the left array
        j = 0  # index into the right array
        k = 0  # Index into the merged array

        # While both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # If the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # If the right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


# Test cases
print("Unsorted: ", items)
mergesort(items)
print("Sorted: ", items)
