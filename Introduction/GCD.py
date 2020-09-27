# Find the greatest common denominator of two numbers
# Using Euclid's algorithms


def gcd(a, b):
    # When b is 0, the gcd is found
    while(b != 0):
        temp = a
        a = b
        # Setting b to be the remainder
        b = temp % b
    return a


# Test cases
print(gcd(60, 96))  # Should be 12
print(gcd(20, 8))  # Should be 4
