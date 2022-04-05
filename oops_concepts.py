""" map real world problems to software solutions """

"""
principles

encapsulation
Inheritance
abstraction
polymorphism

"""

# classes and objects

# clasess are user defined datatypes and act as blue print for our objects where all the methods and variables are defined

# instance method

# getter and setter method also called as accessor and mutator methods

# differenct between mthods and constructors
	# name can be anything : name should be __init__
	# called execute when its invoked. will be executed at creation of the object
	# called any number of times, can be called only once that to at the time of the creation of object thats all, once per obj
	# business logic , declare and initalise the object

# static fields are the fields without the key word self, also can be access without the object mean directly through the Class name

# static methods with a decoratortatic method

# inner class

# garbage collections, garbage collector keeps running at background, when no ref then it clears, also we can write destructor


# destructor __del__

import gc
print(gc.isenabled())

gc.disable()
gc.enable()


class product:

	# static field
	expediture_period = "Monthly"

	# static method

	# constructor method
	def __init__(self,name,usage,price):
		self.name = name
		self.usage = usage
		self.price = price

	def __del__(self):
		print("this is a destructor method")

	# instance method
	def monthly_cost(self):
		if self.usage == "weekly":
			return 4 * self.price
		else:
			return 30 * self.price

	# settor method
	def set_extra_costs(self,expenses):
		self.expenses = expenses

	# getter methods
	def get_extra_costs(self):
		return self.expenses

	@staticmethod
	def year_period():
		print("this is a static method")
		return "nothing"



	# inner class
	class people:
		def __init__(self,peoples):
			self.peoples = peoples

		def display_peoples(self):
			print(self.peoples)




p1 = product("shampoo","weekly",50)
p1.set_extra_costs(900)
print(f"{p1.name} is a product used {p1.usage} and having a price of {p1.price} and having a monthly cost of {p1.monthly_cost()}")

p2 = product("soap","daily",20)
print(f"{p2.name} is a product used {p2.usage} and having a price of {p2.price} and having a monthly cost of {p2.monthly_cost()}")


print(p1.get_extra_costs()) 
print(p1.expediture_period,product.expediture_period)
print(product.year_period())

p1.people(5).display_peoples()


p1 = None
