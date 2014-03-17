import unittest
from solution import count_substring

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(2, count_substring("This is a test string", "is"))
		self.assertEqual(2, count_substring("babababa", "baba"))
		self.assertEqual(4, count_substring("Python is an awesome language to program in!", "o"))
		self.assertEqual(0, count_substring("We have nothing in common!", "really?"))
		self.assertEqual(2, count_substring("This is this and that is this", "this"))
if __name__ == '__main__':
	unittest.main()