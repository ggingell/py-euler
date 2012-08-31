# Find the sum of all the multiples of 3 or 5 below 1000.

f = lambda x: x % 3 == 0 and x or 0
u = lambda x: x % 5 == 0 and x or 0
c = 0

for x in range(1, 1000):
	
	
	print '--------------------------------------------'
	print 'x = ' + str(x)

	k = f(x)
	e = u(x)
	
	print 'k = ' + str(k)
	print 'e = ' + str(e)
  
	if (k > 0) or (e > 0):
  
		if k == e:
			c = c + k
			print 'k=e and, c = ' + str(c)
		else:
			c = c + k
			c = c + e
			print 'k!=e and c = ' + str(c)
	else:
		print 'k = ' + str(k) + ' and e = ' + str(e)
		print 'c should not change ' + str(c)
 
print 'I see the c is equal to: ' + str(c)