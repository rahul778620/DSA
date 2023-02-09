# Given an integer n, return the number of prime numbers that are strictly less than n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

# Sieve of eratosthenes
import math
def countPrimes(self, n: int) -> int:
    prime = [True] * n
    if n < 2:
        return 0
    else:
        prime[0] = prime[1] = False
        for i in range(2, int(math.sqrt(n)) + 1):
            if prime[i]:                
                for j in range(i * i, n, i):
                    prime[j] = False
        return sum(prime)


# Time Complexity: O(n*log(log(n)))

# Auxiliary Space: O(n)
