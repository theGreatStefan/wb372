import scipy.optimize

def root(a, k):
	tol = 1e-15
	i = 1
	f = func(i, a, k)
	fprime = funcprime(i, a, k)
	#lambda f: a*i**b
	#lambda fprime: (a*b)*i**(b-1)
	
	while abs(0 - f) > tol and i<=100:
		i += 1
		#lambda f: a*i**b
		#lambda fprime: (a*b)*i**(b-1)
		x = 1 - f/fprime
		f = func(x, a, k)
		fprime = funcprime(x, a, k)
		
	return x

def func(x, a, k):
	return a*x**k

def funcprime(x, a, k):
	return (a*k)*x**(k-1)
