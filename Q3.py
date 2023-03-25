import csv 
import sqlite3
# create connections 
conn=sqlite3.connect('company.db')
#create cursor to execute sql commands
cur=conn.cursor()

with open ('employees_part_1.csv',newline='') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        cur.execute('''INSERT INTO Employees 
                     (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (row['EMPLOYEE_ID'], row['FIRST_NAME'], row['LAST_NAME'], row['EMAIL'], row['PHONE_NUMBER'], row['HIRE_DATE'], row['JOB_ID'], row['SALARY'], row['MANAGER_ID'], row['DEPARTMENT_ID']))
        
# commit changes and close connection
conn.commit()
conn.close()        