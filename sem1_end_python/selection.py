def sort(L):
	i = 0
	minj = L[0]
	while i<len(L):
		for j in range(i, len(L)):
			if L[j] < L[i]:
				temp = L[i]
				L[i] = L[j]
				L[j] = temp

		i = i+1
			
	print(L)
