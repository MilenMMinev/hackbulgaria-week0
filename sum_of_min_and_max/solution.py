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
def sum_of_min_and_max(arr):
	return min_of_array(arr) + max_of_array(arr)