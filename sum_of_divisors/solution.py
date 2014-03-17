def sum_of_divisors(n):
	result = 0
	for x in range(1,n+1):
		if n % x == 0:
			result = result + x
	return result
