import sqlite3

# create connection to database
conn = sqlite3.connect('Company.db')

# create cursor object to execute SQL commands
cur = conn.cursor()

# delete all employees whose last name is "Chen"
cur.execute('''DELETE FROM Employees WHERE LAST_NAME = ?''', ("Chen",))

# commit changes and close connection
conn.commit()
conn.close()