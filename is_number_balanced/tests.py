import unittest
from solution import is_num_balanced

class TestSolution(unittest.TestCase):
	def test_solution(self):
		self.assertEqual(True, is_num_balanced(9))
		self.assertEqual(True, is_num_balanced(11))
		self.assertEqual(False, is_num_balanced(13))
		self.assertEqual(True, is_num_balanced(121))
		self.assertEqual(True, is_num_balanced(4518))
		self.assertEqual(False, is_num_balanced(28471))
		self.assertEqual(True, is_num_balanced(1238033))
if __name__ == '__main__':
	unittest.main()


	print (is_num_balanced(9))
	print (is_num_balanced(11))
	print (is_num_balanced(13))
	print (is_num_balanced(121))
	print (is_num_balanced(4518))
	print (is_num_balanced(28471))
	print (is_num_balanced(1238033))