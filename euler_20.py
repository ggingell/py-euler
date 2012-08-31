# Find the sum of digits in 100!
# Author: Grant Gingell

f = lambda x: x * (x - 1) != 0 and x or 1
u = 1
c = 0

for x in range(1, 101):
#  print f(x)
  u = u * f(x)
  c = sum(map(int,str(u)))

#print 'u = ' + str(u) 
#print 'c is: ' + str(len(str(u))) + ' digits!'
print 'c = ' + str(c)