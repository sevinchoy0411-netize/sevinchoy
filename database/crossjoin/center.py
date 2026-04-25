from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE center_lerning"
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
#     """CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     """CREATE TABLE teachers(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO students(name) VALUES('Zoxira'),('Valijon'),('Maftuna'),('Ulugbek')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO courses(title) VALUES('KOmpyuter savodxonligi'),('Dasturlash')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO teachers(name) VALUES('Mirzabek'),('Kamolladin')"
# )
# print("Succesfully added")

# cur.execute(
#     "UPDATE courses SET title='Kompyuter savodxonligi' WHERE id=1"
# )

# cur.execute(
#     "SELECT * FROM students CROSS JOIN courses"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

cur.execute(
    "SELECT name FROM students UNION SELECT name FROM teachers;"
)
rows = cur.fetchall()
for row in rows:
    print(row)