#!/usr/bin/python

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	
	def print_me(self):
		print "Type:", self.__class__.__name__
	
## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog's name
		self.name = name
		
	def print_me(self):
		print "Type:", self.__class__.__name__
		print "Name:", self.name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat's name
		self.name = name
		
	def print_me(self):
		print "Type:", self.__class__.__name__
		print "Name:", self.name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person's name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
	def print_me(self):
		print "Type:", self.__class__.__name__
		print "Name:", self.name
		print "Pet:\n", self.pet.print_me()
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## hmm what is this strange magic?
		## call __init__ of Person
		super(Employee, self).__init__(name)
		## Employee's salary
		self.salary = salary
		
	def print_me(self):
		super(Employee, self).print_me()
		print "Type:", self.__class__.__name__
		print "Salary:", self.salary
		
## Fish is-a object
class Fish(object):

	def print_me(self):
		print "Type:", self.__class__.__name__
	
## Salmon is-a Fish
class Salmon(Fish):

	def print_me(self):
		super(Salmon, self).print_me()
	
## Halibut is-a Fish
class Halibut(Fish):

	def print_me(self):
		super(Halibut, self).print_me()

## rover is-a dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet and it is satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet and it is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

#rover.print_me()
#satan.print_me()
mary.print_me()
#frank.print_me()
#flipper.print_me()
#crouse.print_me()
#harry.print_me()
