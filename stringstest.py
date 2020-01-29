# James Ryan

# Python 3.7.1

import unittest
import strings


class MyTestCase(unittest.TestCase):

	def test_1(self):
		test = strings.shorten("",5)
		self.assertEqual("", test)

	def test_2(self):
		test = strings.shorten("Test 2",5)
		self.assertEqual(5, len(test))

	def test_3(self):
		test = strings.shorten("Test 3",6)
		self.assertEqual(6, len(test))

	def test_4(self):
		test = strings.shorten("Test 4",10)
		self.assertEqual(6, len(test))

	def test_5(self):
		test = strings.shorten("sadasdasd dsadsadas asdasdasd asdasdasdas",15)
		self.assertEqual(15, len(test))

	def test_6(self):
		test = strings.shorten("sadasdasd dsadsadas asdasdasd asdasdasdas",15, token="-")
		self.assertEqual(15, len(test))

	def test_7(self):
		test = strings.shorten("sadasdasd dsadsadas asdasdasd asdasdasdas",15, token="-", keep=True)
		self.assertGreaterEqual(15, len(test))

if __name__ == '__main__':
	unittest.main()
