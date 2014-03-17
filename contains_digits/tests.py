import unittest
from solution import contain_digits

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(True, contain_digits(402123, [0, 3, 4]))
		self.assertEqual(False, contain_digits(666, [6,4]))
		self.assertEqual(False, contain_digits(123456789, [1,2,3,0]))
		self.assertEqual(True, contain_digits(456, []))
if __name__ == '__main__':
	unittest.main()