
def is_int_palindrom(n):
	return str(n) == str(n)[::-1]

def main():
	print(is_int_palindrom(1))
	print(is_int_palindrom(42))
	print(is_int_palindrom(100001))
	print(is_int_palindrom(999))
	print(is_int_palindrom(123))
if __name__ == '__main__':
	main()