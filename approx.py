from math import pi,exp
from random import randint

# Sieve the list, searching for the best approximation; i.e the lowest difference (in abs) between the number to be approximated and the approximation.
def sieve1(num, li):
	if len(li) == 0:
		return li
	lq = []
	for i in li:
		n, den = i.split('/')
		n = int(n)
		den = int(den)
		lq.append(abs(num - n/den))
	return li[ lq.index(min(lq)) ]
	
# Approximate an irrational number m as a rational number, given an error ep, an upper bound to search for its approximation numerator and denominator, and the number of iterations iter. This returns a string that represents the fraction.
def approx(m,ep,up=100,iter=1000):
	res = []
	for _ in range(iter):
		a = randint(1,up)
		b = randint(2,up)
		if abs(m - a/b) < ep:
			res.append(f"{a}/{b}")
	return sieve1(m,res)
			
"""
approximate phi (golden ratio)
b = (1+5**0.5)/2
for _ in range(100):
    a=approx(b,0.001,up=500,iter=2000)
    if len(a)!=0:
	    print(a)
	    break
"""
