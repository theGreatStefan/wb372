def linsearch(l, x):
	i = 0
	listx = []
	newitem = [0]
	counter = 0
	while i < len(l):
		if (x == l[i]):
			newitem[0] = i
			listx = listx + newitem
			

		i = i+1
	if (len(listx) > 0):
		return listx
	else:
		print "NOOOOPE"
