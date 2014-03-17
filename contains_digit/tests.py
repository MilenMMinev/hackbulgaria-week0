import unittest
from solution import digit_is_in_number

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(False, digit_is_in_number(123, 4))
		self.assertEqual(True, digit_is_in_number(42, 2))
		self.assertEqual(True, digit_is_in_number(1000, 0))
		self.assertEqual(False, digit_is_in_number(12346789, 5))
if __name__ == '__main__':
	unittest.main()