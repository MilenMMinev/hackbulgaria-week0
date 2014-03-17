import unittest
from solution import vowels_in_string

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(2, vowels_in_string("Python"))
		self.assertEqual(8, vowels_in_string("Theistareykjarbunga"))
		self.assertEqual(0, vowels_in_string("grrrrgh!"))
		self.assertEqual(22, vowels_in_string("Github is the second best thing that happend to programmers, after the keyboard!"))
		self.assertEqual(8, vowels_in_string("A nice day to code!"))
if __name__ == '__main__':
	unittest.main()