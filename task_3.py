import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="Employee"
)

mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
)
""")

data = [
    (1, 'Arpit', 'AI', 75000),
    (2, 'Ankit', 'HR', 55000),
    (3, 'Divya', 'IT', 60000),
    (4, 'Ritika', 'HR', 44000),
    (5, 'Ayush', 'Finance', 45000)
]

mycursor.executemany("""
INSERT INTO employees (id, name, department, salary)
VALUES (%s, %s, %s, %s)
""", data)

mydb.commit()

query = "SELECT * FROM employees"

df = pd.read_sql(query, mydb)

# Display 
print(df)