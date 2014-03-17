import unittest
from solution import is_int_palindrom

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(True, is_int_palindrom(1))
		self.assertEqual(False, is_int_palindrom(42))
		self.assertEqual(True, is_int_palindrom(100001))
		self.assertEqual(True, is_int_palindrom(999))
		self.assertEqual(False, is_int_palindrom(123))
if __name__ == '__main__':
	unittest.main()
