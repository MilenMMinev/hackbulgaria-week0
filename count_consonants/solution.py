def vowels_in_string(str):
	sum = 0
	for item in str.lower():
		if (item == 'b') or (item == 'c') or (item == 'd') or (item == 'f') or (item == 'g') or (item == 'h') or (item == 'j') or (item == 'k') or (item == 'l') or (item == 'm') or (item == 'n') or (item == 'p') or (item == 'q') or (item == 'r') or (item == 's') or (item == 't') or (item == 'v') or (item == 'w') or (item == 'x') or (item == 'z'):
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