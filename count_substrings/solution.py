def count_substring(heystack, needle):
	return heystack.count(needle)

def main():
	print (count_substring("This", "This"))
	print (count_substring("This is a test string", "is"))
	print (count_substring("babababa", "baba"))
	print (count_substring("Python is an awesome language to program in!", "o"))
	print (count_substring("We have nothing in common!", "really?"))
	print (count_substring("This is this and that is this", "this"))
if __name__ == '__main__':
	main()