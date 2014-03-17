import time
def is_prime(n):
	if n < 2:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	return True

def prime_divs(n):
	divs = []
	for item in range(n):
		if is_prime(item) and n % item == 0:
			divs.append(item)
	return divs


def prime_factorization(n):
	if is_prime(n):
		return (n, 1)
	result = []
	for i in prime_divs(n):
		for j in prime_divs(n):
			for k in range (0, 12):
				for l in range (0, 12):
					if (i ** k) * (j ** l) == n:
						result =(i, k), (j, l)
		return result