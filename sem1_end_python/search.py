def search(l, x):
	bhalf = []
	thalf = []
	i = 0

	length = len(l)
	hi = length
	lo = 0

	bhalf = l[lo:length/2]
	thalf = l[(length/2)+1:length]
	
	if (x < thalf[0]):
		search(thalf, x)
