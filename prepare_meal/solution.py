def find_largest_devider(number):
	n = 1
	for item in range (0 ,number):
		if number % (3 ** item) == 0:
			n = item
	return n

def divides_by_5(number):
	if number % 5 == 0:
		return True
	return False

def prepare_meal(number):
	string = ""
	for x in range(0,find_largest_devider(number)):
		string = string + "spam "
	if divides_by_5(number):
		if string == '':
			string = string + 'eggs'
		else:
			string = string + "and eggs"
	return string