class Solution:
	def PowMod(self, x, n, m):
		# Code here
		res = 1
		while n > 0 :
		    if n & 1 :
		        res = (res * x) % m
		    n >>= 1
		    x = (x ** 2 ) % m
	    return res
