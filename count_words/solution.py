def count_occurances(string, arr):
	count = 0
	for item in arr:
		if string == item:
			count = count + 1
	return count


def count_words(arr):
	d = {}
	for item in arr:
		d[item] = count_occurances(item, arr)
	return d