def sevens_in_a_row(arr, n):
	count_of_sevens = 0
	for item in arr:
		if item == 7:
			count_of_sevens = count_of_sevens + 1
	if count_of_sevens >= n:
		return True
	return False

