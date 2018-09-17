def neville(x_data, y_data, x):
	"""p = neville(x_data, y_data, x) 
		Evaluate the polynomial interpolant p(x) that passes through the 
		specified data points by Neville's method."""

	k = len(x_data)-1
	if k<1 :
		return x_data

	part1 = (x - x_data[k])*x_data[0:k-1]
	
	part2 = (x_data[0] - x)*x_data[1:k]

	divBy = (x_data[0] - x_data[k])

	P = (part1 + part2)
	P = P[0:len(P)-1] * (1/divBy)

	return neville(P, y_data, x)		
