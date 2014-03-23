import solution
import unittest


class TestSolution(unittest.TestCase):

	def test_solution(self):
		self.assertEqual([(2,2)], solution.goldbeach(4))
		self.assertEqual([(3,3)], solution.goldbeach(6))
		self.assertEqual([(3,5)], solution.goldbeach(8))
		self.assertEqual([(3,7), (5,5)], solution.goldbeach(10))
		self.assertEqual([(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)], solution.goldbeach(100))

if __name__ == '__main__':
	unittest.main()