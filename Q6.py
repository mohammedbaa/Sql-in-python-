import sqlite3

# create connection to database
conn = sqlite3.connect('Company.db')

# create cursor object to execute SQL commands
cur = conn.cursor()

# update salary of employee with id=109 to 9500
cur.execute('''UPDATE Employees SET SALARY = ? WHERE EMPLOYEE_ID = ?''', (9500, 109))

# commit changes and close connection
conn.commit()
conn.close()