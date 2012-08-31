# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 20! = 2432902008176640000

# Function that determines if p is a factor of q
is_factor = lambda p,q: q % p == 0 and p or 0

i = 10 # Start here to avoid getting 0 as an answer
while i <= 10000000:
  divisor = 2
  print "START---------------------------------"
  print "i: " + str(i)
  while is_factor(divisor, i) == divisor:
    if divisor == 10:
      print i
      break
    else:
      print "divisor += 1: " + str(divisor)
      divisor += 1


  i += 10
  print "END-----------------------------------"
  print "\n"