import unittest
from solution import vowels_in_string

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(4, vowels_in_string("Python"))
		self.assertEqual(11, vowels_in_string("Theistareykjarbunga"))
		self.assertEqual(7, vowels_in_string("grrrrgh!"))
		self.assertEqual(44, vowels_in_string("Github is the second best thing that happend to programmers, after the keyboard!"))
		self.assertEqual(6, vowels_in_string("A nice day to code!"))
if __name__ == '__main__':
	unittest.main()