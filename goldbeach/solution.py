import time

def is_prime(n):
	if n < 2:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	return True


def goldbeach (n):
	result = []
	for i in range (2,n+1):
		for j in range (2, n+1):
			if i + j == n and n % 2 == 0 and is_prime(i) and is_prime(j) and i <= j:
				pair = i, j
				result.append(pair)
	return result