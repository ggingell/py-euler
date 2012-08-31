# Find the sum of even valued terms of fib that are < 4 million
# Author: Grant Gingell

f = 0
u = 1
c = 0
k = 4000000
e = lambda x: (x % 2 == 0 and x < k) and x or 0

for x in range(0, 50):
  print e(u)
  c = c + e(u)
  c = c + e(f)
  f = u + f
  u = f + u
  print str(e(f)) + ' and c = ' + str(c)
  print '---------------------------------'


print 'c = ' + str(c) 
