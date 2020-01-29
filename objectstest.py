# James Ryan

# Python 3.7.1

import unittest
import objects
import objects_item


class MyTestCase(unittest.TestCase):
	"""
	Runs before each test
	"""
	def setUp(self):
		self.test = objects.objects()

		self.test.add("first_name", "John")
		self.test.add("last_name", "Doe")
		self.test.add("phone", "5555555555")
		self.test.add("address", "1234 Test St")

	"""
	Tests the override of function __len__ in objects
	"""
	def test_length(self):
		self.assertEqual(4, len(self.test))

	"""
	Tests adding an object to the dictionary
	"""
	def test_add(self):
		self.test.add("middle_name", "Bob")
		self.assertEqual(5, len(self.test))
		self.assertEqual(self.test.getValue("middle_name"), "Bob")

	"""
	Tests adding an object with duplicate key to the dictionary
	"""
	def test_add_duplicate_key(self):
		with self.assertRaises(Exception) as context:
			self.test.add("first_name", "Bob")
			self.assertTrue("Key already Exists." in str(context.exception))

	"""
	Tests removing an object from the dictionary that exists
	"""
	def test_remove_exists(self):
		self.test.remove("last_name")
		self.assertEqual(3, len(self.test))

	"""
	Tests removing an object from the dictionary that doesn't exist
	"""
	def test_remove_not_exists(self):
		self.test.remove("last_na")
		self.assertEqual(4, len(self.test))

	"""
	Tests poping an existing object from the dictionary
	"""
	def test_pop_exists(self):
		object = self.test.pop("last_name")
		self.assertEqual(str(object),
						 str(objects_item.objects_item("last_name", "Doe")))

	"""
	Tests popping an object with a non-existant key from the dictionairy
	"""
	def not_pop_not_exists(self):
		object = self.test.pop("last_name")
		self.assertEqual(object,None)

	"""
	Tests the override of the __str__ function
	"""
	def test_toString(self):
		self.assertEqual(str(self.test), "['first_name : John', " +
			"'last_name : Doe', " +
			"'phone : 5555555555', " +
			"'address : 1234 Test St']")

	"""
	Tests the retreiving and modification of the value history
	"""
	def test_testHistory(self):
		self.test.changeValue("phone", "1111111111")
		self.assertEqual(self.test.getValue("phone"), "1111111111")
		self.assertEqual(self.test.getHistory("phone"), ["5555555555"])
		self.test.changeValue("phone", "2222222222")
		self.assertEqual(self.test.getValue("phone"), "2222222222")
		self.assertEqual(self.test.getHistory("phone"), ["1111111111", "5555555555"])

	"""
	Tests changing the value of an object in the dictionary using it's key
	"""
	def test_changeValue(self):
		self.test.changeValue("phone", "1111111111")
		self.assertEqual(self.test.getValue("phone"), "1111111111")


if __name__ == '__main__':
	unittest.main()
