# Variable Declaration

x =  10
print x 


#  GET address of a variable

x = 5
print hex(id(x))

# ===================================


# print range(10,20)

def checkprimenumbers(min, max):

	for num in range(min,max):

		print range(2,num)

		for i in range(2, num):

			if num%i == 0:

				j = num/i

				print '%d equals %d * %d' % (num,i,j)

				break

			else:

				print num, 'is a prime number'

				break


# checkprimenumbers(10, 20)


def functionprime(num):
	i = 2
	while(i < num):
	   j = 2
	   while(j <= (i/j)):
	      if not(i%j): break
	      j = j + 1
	      
	   if (j > i/j) : print i, " is prime"
	   i = i + 1

	print "Good bye!"

# functionprime(100)