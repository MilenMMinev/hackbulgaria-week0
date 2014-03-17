import unittest
from solution import prime_number_of_divisors

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(True, prime_number_of_divisors(7))
		self.assertEqual(False, prime_number_of_divisors(8))
		self.assertEqual(True, prime_number_of_divisors(9))
if __name__ == '__main__':
	unittest.main()
