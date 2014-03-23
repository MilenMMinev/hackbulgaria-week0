import unittest
import solution


class TestSolution(unittest.TestCase):
	def test_is_an_bn(self):
		self.assertFalse(solution.is_word_anbn(""))
		self.assertFalse(solution.is_word_anbn("rado"))
		self.assertFalse(solution.is_word_anbn("aaabb"))
		self.assertTrue(solution.is_word_anbn("aaabbb"))
		self.assertFalse(solution.is_word_anbn("aabbaabb"))
		self.assertFalse(solution.is_word_anbn("bbbaaa"))
		self.assertTrue(solution.is_word_anbn("aaaaabbbbb"))
		self.assertFalse(solution.is_word_anbn("baba"))
if __name__ == '__main__':
	unittest.main()