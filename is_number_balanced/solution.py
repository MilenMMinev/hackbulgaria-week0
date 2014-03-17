def count_digits(n):
	sum = 0
	while n != 0:
		n = n // 10
		sum = sum + 1
	return sum

def sum_last(n):
	sum = 0
	for item in range(0,(count_digits(n) // 2)):
		sum = sum + n % 10
		n = n // 10
	return sum

def sum_first(n):
	sum = 0
	if count_digits(n) % 2 == 0:
		n = n // 10 ** (count_digits(n) // 2)
		while n != 0:
			sum = sum + n % 10
			n = n // 10
	if count_digits(n) % 2 == 1:
		n = n // 10 ** ((count_digits(n) // 2)+1)
		while n != 0:
			sum = sum + n % 10
			n = n // 10
	return sum
			

def is_num_balanced(n):
	return sum_first(n) == sum_last(n)

def main():
	print (is_num_balanced(9))
	print (is_num_balanced(11))
	print (is_num_balanced(13))
	print (is_num_balanced(121))
	print (is_num_balanced(4518))
	print (is_num_balanced(28471))
	print (is_num_balanced(1238033))
if __name__ == '__main__':
	main()