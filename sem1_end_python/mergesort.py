def mergesort(l):
	if (len(l)<=1):
		return

	mid = len(l)/2

	left = l[:mid]
	right = l[mid:]

	mergesort(left)
	mergesort(right)

	l[:] = merge(left,right)


def merge(l1,l2):
	ls = []
	i1 = i2 = 0
	while i1 < len(l1) and i2 < len(l2):
		if (l1[i1] <= l2[i2]):
			ls.append(l1[i1])
			i1 = i1 +1
		else:
			ls.append(l2[i2])
			i2 = i2 + 1

	ls.extend(l1[i1:])
	ls.extend(l2[i2:])

	return ls
