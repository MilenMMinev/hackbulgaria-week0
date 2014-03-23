def is_word_anbn(string):
	new = list(string)
	if len(string) % 2 != 0 or len(string) < 2:
		return False
	half = len(new) // 2
	first_half = new[half:]
	second_half = new[:half]
	for i in first_half:
		if i != 'b':
			return False
	for j in second_half:
		if j != 'a':
			return False
	return True
