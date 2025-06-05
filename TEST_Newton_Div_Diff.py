from Newton_Div_Diff import *
import random
import time

LIM = 200 # the magnitude for random values
DIM = 200 # the size for random lists of random values
N = 200 # the number of random tests


print("--------------------------------FILE: TEST_Newton_Div_Diff.py--------------------------------")
print("this tests that the polynomial samples")
print("and the interpolation of those samples")
print("match each other")
print(f"Testing random magnitudes {LIM} sizes {DIM} of length {N}")
print(time.ctime())
print(time.strftime('%Y.%m.%d.%H%M%S'))
dtime = time.time()
count = 0
for i in range(N):
	coeff_list = [random.randint(-LIM, LIM) for _ in range(DIM)]
	xlist = random.sample(range(-LIM, LIM + 1), DIM + 1) # a set of random values, no repeated values, of enough dim to interpolate
	ylist = []
	for x in xlist: # interpolate an existing polynomial in order to avoid fractions in the calculations
		ylist.append(eval(coeff_list, x))
	pp = ndd(xlist, ylist) # now interpolate the polynomial
	for j in range(DIM):
		diff = coeff_list[j] - pp[j]
		if diff != 0: print(".", end="")
		else: count = count + 1
	#print(y)
	#print(yy)

dtime = time.time() - dtime
print("Time taken overall:", dtime)
print("Total values checked and good:", count)
