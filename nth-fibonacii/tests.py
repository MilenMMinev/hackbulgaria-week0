import unittest
from solution import nthFib

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(1, nthFib(1))
		self.assertEqual(1, nthFib(2))
		self.assertEqual(2, nthFib(3))
		self.assertEqual(55, nthFib(10))
if __name__ == '__main__':
	unittest.main()
