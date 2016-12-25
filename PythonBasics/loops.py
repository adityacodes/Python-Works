
# The @continue 
# statement rejects all the remaining statements in the 
# current iteration of the loop and moves 
# the control back to the top of the loop.

def executecontinue():
	for letter in 'Python':     # First Example
	   if letter == 'h':
	      continue
	   print 'Current Letter :', letter


# The @pass statement is a null operation; 
# nothing happens when it executes. 

def executepass():
	for letter in 'Python': 
	   if letter == 'h':
	      pass
	      print 'This is pass block'
	   print 'Current Letter :', letter

	print "Good bye!"


# The @break statement
# Terminates the loop statement and transfers execution to the statement immediately following the loop.

def executebreak():

	for letter in 'Python':     # First Example
	   if letter == 'h':
	      break
	   print 'Current Letter :', letter
	  
	var = 10                    # Second Example
	while var > 0:              
	   print 'Current variable value :', var
	   var = var -1
	   if var == 5:
	      break

	print "Good bye!"


# executebreak()
# executepass()
# executecontinue()