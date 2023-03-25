import json
import sqlite3

# create connection to database
conn = sqlite3.connect('Company.db')

# create cursor object to execute SQL commands
cur = conn.cursor()

# open JSON file and read contents
with open('employees_part_2.json') as jsonfile:
    data = json.load(jsonfile)
    for row in data:
        # insert row data into employees table
        cur.execute('''INSERT INTO Employees 
                       (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (row['EMPLOYEE_ID'], row['FIRST_NAME'], row['LAST_NAME'], row['EMAIL'], row['PHONE_NUMBER'], row['HIRE_DATE'], row['JOB_ID'], row['SALARY'], row['MANAGER_ID'], row['DEPARTMENT_ID']))

# commit changes and close connection
conn.commit()
conn.close()