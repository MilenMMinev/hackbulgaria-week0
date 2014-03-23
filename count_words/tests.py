import solution
import unittest


class TestSolution(unittest.TestCase):

	def test_solution(self):
		self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, solution.count_words(["apple", "banana", "apple", "pie"]))
		self.assertEqual({'ruby': 1, 'python': 3}, solution.count_words(["python", "python", "python", "ruby"]))

if __name__ == '__main__':
	unittest.main()