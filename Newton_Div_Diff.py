
def eval(coeff_list, n): ## make a number, i.e. evaluate, polynomial list p
	lenp = len(coeff_list)
	y = 0
	for i in range(lenp-1, -1, -1):
		y = y*n + coeff_list[i] # y*n first in case it is a poly type, then the integer self.list[i] can be added
	return y

def ndd(xlist, ylist):
	"""
	Newton's Divided Differences interpolation of polynomial values (x, y)
	"""
	assert len(xlist) == len(ylist), "divided_differences(): The lists must be of same dimension!"
	n = len(xlist)
	for i in range(n - 1): # check the input list for uniqueness
	  for j in range(i + 1, n):
	    if xlist[i] == xlist[j]:
	      print("ERROR: items in xlist are not unique!!!")
	      return []
	cc = ylist[:] # copy the ylist elements to use as in-place operations
	for i in range(n - 1):
		for j in range (n - 1, i, -1):
			cc[j] = (cc[j] - cc[j - 1])//(xlist[j] - xlist[j - i - 1])
	for i in range(n - 1):
		for j in range(n - 2, i - 1, -1):
			cc[j] -= xlist[j - i]*cc[j + 1]
	return cc
