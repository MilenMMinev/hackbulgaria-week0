def count_occurances(string, arr):
	count = 0
	for item in arr:
		if string == item:
			count = count + 1
	return count

def has_duplicate(string, arr):
	if count_occurances(string, arr) > 1:
		return True
	return False

def unique_words_count(arr):
	uniques = -1
	for item in arr:
		if has_duplicate(item, arr):
			uniques= uniques + 1
	return len(arr) - uniques


def main():
	print(unique_words_count(["apple", "banana", "apple", "pie"]))
	print(unique_words_count(["python", "python", "python", "ruby"]))
	print(unique_words_count(["HELLO!"] * 10))
if __name__ == '__main__':
	main()