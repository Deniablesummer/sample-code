# James Ryan

# Python 3.7.1

import objects_item


class objects:

	"""
	Constructor for objects 'dictionary' like data structure
	"""
	def __init__(self):
		self.__myList = []

	"""
	Used to add a key/value pair to the dictionary
	"""
	def add(self, key, value):
		for item in self.__myList:
			if item.getKey() == key:
				raise Exception("Key Already Exists.")
		temp = objects_item.objects_item(key, value)
		self.__myList.append(temp)

	"""
	Used to remove a key/value pair from the dictionairy using it's key
	"""
	def remove(self, key):
		ind = 0
		for item in self.__myList:
			if item.getKey() == key:
				self.__myList.pop(ind)
				return
			ind = ind + 1
		return


	"""
	Used to retreive the value of an object in the dictionary
	Returns: objects_item.__value
	"""
	def getValue(self, key):
		for item in self.__myList:
			if item.getKey() == key:
				return item.getValue()

	"""
	Used to change the value of an object in the dictionary using it's key
	"""
	def changeValue(self, key, value):
		for item in self.__myList:
			if item.getKey() == key:
				item.setValue(value)

	"""
	Used to pop an object in the dictionary
	Returns: objects_item
	"""
	def pop(self, key):
		ind = 0
		for item in self.__myList:
			if item.getKey() == key:
				return self.__myList.pop(ind)
			ind = ind + 1
		return None
	"""
	Used to retreive the history of an object in the dictionary
	Returns: list of previous values
	"""
	def getHistory(self, key):
		for item in self.__myList:
			if item.getKey() == key:
				return item.getHistory()

	"""
	Overrides the __str__ function for the dictionary to return 
	'[key : value, key : value, ...]
	"""
	def __str__(self):
		temp = []
		for item in self.__myList:
			temp.append(str(item))
		return str(temp)

	"""
	OVerrides the __len__ function for the dictionary"""
	def __len__(self):
		return len(self.__myList)

