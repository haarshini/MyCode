def Sum(m,n):
	p=0
	s=0
	for i in range(0,n):
		for j in range(0,n):
			if i == j:
				p += m[i][j]

			if i+j == n-1 :
				s += m[i][j]
	print("diff:",abs(p-s))
a= [[11,2,4],[4,5,6],[10,8,-12]]

Sum(a,3)
