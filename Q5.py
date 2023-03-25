import sqlite3

# create connection to database
conn = sqlite3.connect('Company.db')

# create cursor object to execute SQL commands
cur = conn.cursor()

# select all employees who work for department_id = 30
cur.execute('''SELECT * FROM Employees WHERE DEPARTMENT_ID = ?''', (30,))
rows = cur.fetchall()

# print the retrieved rows
for row in rows:
    print(row)

# close connection
conn.close()