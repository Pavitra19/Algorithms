// Find the greatest common denominator of two numbers
// Using Euclid's algorithms

const gcd = (a, b) => {
    // When b is 0, the gcd is found
    while (b !== 0) {
        var temp = a
        a = b
        // Setting b to be the remainder
        b = temp % b
    }

    return a;

}

// Test cases
console.log(gcd(60, 96)) // Should be 12
console.log(gcd(20, 8)) // Should be 4
console.log(gcd(2, 7)) // should be 1
