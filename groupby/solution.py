def groupby(function, sequence):
	result = {}
	for x in sequence:
		if function(x) in result:
			result[function(x)].append(x)
		else:
			result[function(x)] = [x]
	return result