from db import connect_db

conn = connect_db()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE students"
# )
# print("Created")

# cur.execute(
    # """CREATE TABLE students(
    # id SERIAL PRIMARY KEY,
    # name VARCHAR(100),
    # score INT
    # )"""
# )
# print("Created")

# cur.execute(
    # "INSERT INTO students(name,score) VALUES('Ixlosbek',95),('Abduvaid',100),('Humoyun',75),('Golibjon',56),('Rayhona',97),('Sevinchoy',100)"
# )
# print("ok")

# cur.execute(
#     "SELECT * FROM students WHERE score = 97"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE score >= 97"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE score <= 97"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE score != 97"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE score <> 97"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students ORDER BY name"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students ORDER BY score"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students ORDER BY name DESC"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students ORDER BY score DESC"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students LIMIT 3"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE name ILIKE 'r%'"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)