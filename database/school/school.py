from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE school"
# )
# print("Database created")

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     """CREATE TABLE teachers(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     subject VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO teachers(name,subject) VALUES('Mirzabek','backend'),('Kamoladdin','frontend')"
# )
# print("Succesfully added")

# cur.execute(
#     "SELECT * FROM students CROSS JOIN teachers"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

cur.execute(
    "SELECT name FROM students UNION SELECT name FROM teachers"
)
rows = cur.fetchall()
for row in rows:
    print(row)