# What is the first term in the Fibonacci sequence to contain 1000 digits?


def fib_r(n):
	if(n<=1):
		return n
	else:
		return fib_r(n-1) + fib_r(n-2)

a, b = 0,1

int_length = lambda integer: len(str(integer))

for i in range(1, 3000):
	if(int_length(fib_r(i)) == 8):
		print i
	
	

#if __name__ == '__main__':
#  print fib_r(10)