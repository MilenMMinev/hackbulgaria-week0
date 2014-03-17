import unittest
from solution import is_increasing

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(True, is_increasing([1,2,3,4,5]))
		self.assertEqual(True, is_increasing([1]))
		self.assertEqual(False, is_increasing([5,6,-10]))
		self.assertEqual(False, is_increasing([1,1,1,1]))
if __name__ == '__main__':
	unittest.main()