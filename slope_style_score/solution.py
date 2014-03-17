def min_of_array(arr):
	smallest = arr[0]
	for item in arr:
		if item < smallest:
			smallest = item
	return smallest

def max_of_array(arr):
	largest = arr[0]
	for item in arr:
		if item > largest:
			largest = item
	return largest

def find_sum(arr):  # sum without the largest and smalelst
	sum = 0
	for item in arr:
		sum = sum + item
	return sum - max_of_array(arr) - min_of_array(arr)

def slope_style_score(scores):
	num = find_sum(scores) / (len(scores)-2)
	num = num * 100
	num = int(num)
	return num / 100

