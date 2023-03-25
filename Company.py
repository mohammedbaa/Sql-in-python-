import sqlite3

# create connection to database
conn = sqlite3.connect('Company.db')

# create cursor object to execute SQL commands
cur = conn.cursor()

# create employees table with columns: EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID
cur.execute('''CREATE TABLE Employees
               (EMPLOYEE_ID INTEGER PRIMARY KEY,
                FIRST_NAME TEXT,
                LAST_NAME TEXT,
                EMAIL TEXT,
                PHONE_NUMBER TEXT,
                HIRE_DATE TEXT,
                JOB_ID TEXT,
                SALARY REAL,
                MANAGER_ID INTEGER,
                DEPARTMENT_ID INTEGER)''')

# commit changes and close connection
conn.commit()
conn.close()

