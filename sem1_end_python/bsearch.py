def search(l, x):
	bhalf = []
	thalf = []
	i = 0

	length = len(l)
	hi = length
	lo = 0

	while (hi > lo):
		mid = (hi + lo)/2

		if (x < l[mid]):
			hi = mid - 1
		elif (x > l[mid]):
			lo = mid + 1
		else:
			return mid

	return "Not found"
