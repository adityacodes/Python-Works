class fruits:
	
	fruitcount = 0

	def __init__(self, name, arg):
		self.arg = arg
		self.name = name
		fruits.fruitcount+=1

	def fprop(self):
		print self.name
		print self.arg
		print fruits.fruitcount

	def fprop(self, name):
		print name

# mango = fruits('Mango', 100)
# mango.fprop()

# orange = fruits('Orange', 200)
# orange.fprop()
# orange.fprop('orange')




# =================================================
# Inheritance


class Parent:        # define parent class
   __parentAttr = 100   # Adding "__" to the beginning of the datamember makes the variable private
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method
# print c._Parent__parentAttr # Accessing private variables using object._classname__datamember



# ==============================================
# Overriding

class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
c.myMethod()         # child calls overridden method


# ==============================================
# Data Hiding


class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
# print counter.__secretCount  ---> This will produce an error since it is a private data member
print counter._JustCounter__secretCount


