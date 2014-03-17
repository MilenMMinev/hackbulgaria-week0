def vowels_in_string(str):
	sum = 0
	for item in str.lower():
		if (item == 'o') or (item == 'a') or (item == 'u') or (item == 'i') or (item == 'e') or (item == 'y'):
			sum = sum + 1
	return sum
def main():
	print (vowels_in_string("Python"))
	print (vowels_in_string("Theistareykjarbunga"))
	print (vowels_in_string("grrrrgh!"))
	print (vowels_in_string("Github is the second best thing that happend to programmers, after the keyboard!"))
	print (vowels_in_string("A nice day to code!"))
if __name__ == '__main__':
	main()