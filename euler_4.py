# A palindromic number reads the same both ways.
# The largest palindrome made from the product of 
# two 2-digit numbers is 9009 = 91  99.

# Find the largest palindrome made from the product of two 3-digit numbers.
# 999^2 = 998001



a = list(range(1,999))
set = []
for x in a:
	for y in a:
		set.append(x*y)
        
# find if a number is palindromey
p = lambda x: str(x) == str(x)[::-1] and x or 0

palins = []
for i in set:
	o = p(i)
	if o != 0:
		palins.append(o)

print max(palins)
