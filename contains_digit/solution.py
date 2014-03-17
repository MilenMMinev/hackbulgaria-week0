def digit_is_in_number(number, digit):
	while number != 0:
		if number % 10 == digit:
			return True
		number = number // 10
	return False
