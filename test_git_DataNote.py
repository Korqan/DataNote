class Person:
	def _init_(self, name, age):
		self.name = name
		self.age = age
	def detail(self):
		print (self.name)
		print (self.age)

obj1 = Person('test1', 12)
print (obj1.name)

obj1.detail()
