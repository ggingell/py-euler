# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural 
# numbers and the square of the sum.

sumSquares = 0 # The sum of each integer after it has been squared.
squaredSums = 0 # The integers are summed and then squared.

for i in range(1,101):
  sumSquares += (i**2)
  squaredSums += i

print (squaredSums**2) - sumSquares
  