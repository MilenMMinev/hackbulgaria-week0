
def calculate_coins(sum):
	coins = [100, 50, 20, 10, 5, 2, 1]
	result = dict()
	sum = sum * 100
	sum = int(sum)
	for item in coins:
		result[item] = sum // item
		sum = sum - item * result[item]
	return result



	return coins
def main():
	print (calculate_coins(123))

if __name__ == '__main__':
	main()