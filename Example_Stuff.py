SQL = "INSERT INTO authors (name) VALUES (%s);" # Note: no quotes
data = ("O'Reilly", )
cur.execute(SQL, data) # Note: no % operator

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"