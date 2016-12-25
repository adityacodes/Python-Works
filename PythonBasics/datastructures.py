
# Lists - [11, 12, 13] - Can be changed appended and extended. 

# Tuple - (10, 20, 20) - Cannot be changed.

# Dictionary - Associative array - {}

# ===============================================================

# Working with Dictionaries

dictionary = { 'name' : 'Aditya Padhi', 'regdno' : '1401106577'}

#remove entry with key name : del dictionary['name']
# print dictionary['name']
# print dictionary['regdno']

for key, val in dictionary.items():
	print key +" : " +val


#  ==============================================================

#  LIST -> TUPLE || TUPLE -> LIST || List-> DICTIONARY

aList = [10,20,20] 
print tuple(aList)

aTuple = (10, 20, 30)
print list(aTuple)

aList1 = [10,20] # Can contain only 2 elements to form a dictionary.
print dict([aList1])

aTuple1 = (10, 20)
print dict([aTuple1])


# ===============================================================
# @TUPLES
# Remember always keep final values in tuples as they cannot be changed
# print maximum value from a tuple

tuple1  = (123, 'xyz', 'zara', 'abc')
tuple2 = (456, 700, 200)

# print max(tuple2)
# print min(tuple1)
# print len(tuple1)
# print cmp(tuple1, tuple2)


# ===============================================================
# @LISTS

list1 = ['banana', 'apple',  'mango']
# print len(list1)
# print range(len(list1))   
# for index in range(len(list1)):
   # print 'Current fruit :', list1[index]


# This prints the index of each element in list1 list

# ===============================================================