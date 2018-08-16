def eval_poly(a, xs, x):
	"""p = eval_poly(a, xs, x)
	   Evaluate Newtons polynomial p at x. Compute the coefficient vector as by calling the function coefficients."""
	n = len(xs) - 1 #degree of polynomial
	p = a[n]
	for k in range(1, n + 1):
		p = a[n-k] + (x - xs[n-k])*p
	return p

def coefficients(xs, ys):
	"""a = coefficients(xs, ys) 
	   Compute the coefficients of Newtons polynomial."""
	m = len(xs) #number of data points
	a = ys.copy()
	for k in range(1, m):
		a[k:m] = (a[k:m] - a[k-1])/(xs[k:m] - xs[k-1])
	return a
