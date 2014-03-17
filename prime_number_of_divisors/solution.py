def is_prime(n):
	if n < 2:
		return False
	for x in range(2,n):
		if n % x == 0:
			return False
	return True

def prime_number_of_divisors(n):
	count = 0
	for item in range(1,n+1):
		if n % item == 0:
			count = count + 1

	return is_prime(count)

