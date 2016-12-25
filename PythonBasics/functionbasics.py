
# function without parameters
def function1():
	print 'This is function without parameters'

# Call to funciton
#function1()




# function with parameters
def function2(x):
	print 'Hello this is '+ x

# function2('Aditya')




#function with more than two and return
def function3(x, y):
	return int(x)+int(y)	


# print function3('10', '12')


# Iterating through lists and printing the elements inside

z = [['10', '11', '12'], ['13', '14', '15']]


def function4(z):
	for x in z:
		for y in x:
			print y

# function4(z)


# Variable length arguments

def printfunction( argument, *varargument):
	print "Output is:"
	print argument
	for v in varargument:
		print v

# printfunction(10, 20,30,40) 


# Scope of variables inside 

total = 0;  # This is global variable.

def sum( arg1, arg2 ):
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

# Now you can call sum function
# sum( 10, 20 );
# print "Outside the function global total : ", total 



