# James Ryan

# Python 3.7.1

class objects_item:

	def __init__(self, key, value):
		self.__key = key
		self.__value = value
		self.__history = []

	"""
	Getter fuction to retreive the value
	"""
	def getValue(self):
		return self.__value

	"""
	Setter function to set the value
	"""
	def setValue(self, value):
		self.__history.insert(0,self.__value)
		self.__value = value

	"""
	Getter funtion to retreive the value history
	"""
	def getHistory(self):
		return self.__history

	"""
	Getter function to retreive the key for the object
	"""
	def getKey(self):
		return self.__key

	"""
	Overrides the ___str__ to return 'key : value'
	"""
	def __str__(self):
		return self.__key + " : " + self.__value

