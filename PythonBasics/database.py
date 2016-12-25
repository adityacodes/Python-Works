
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM `hello`")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

for key in data:
	print dict([key])



# print data

# disconnect from server
db.close()