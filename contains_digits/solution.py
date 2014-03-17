def digit_is_in_number(number, digits):
	while number != 0:
		if number % 10 == digits:
			return True
		number = number // 10
	return False


def contain_digits(number, digits):
	for item in digits:
		if not digit_is_in_number(number, item):
			return False
	return True


def main():
	print (contain_digits(402123, [0, 3, 4]))
	print (contain_digits(666, [6,4]))
	print (contain_digits(123456789, [1,2,3,0]))
	print (contain_digits(456, []))
if __name__ == '__main__':
		main()