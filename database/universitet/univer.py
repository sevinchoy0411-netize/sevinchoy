from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE universitet"
# )
# print("Database created")

# cur.execute(
#     """
#     CREATE TABLE talabalar(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE kurslar(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE enrolments(
#     student_id INTEGER,
#     course_id INTEGER
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO talabalar (name) VALUES ('Fotima')"
# )

# cur.execute(
#     "INSERT INTO kurslar (name) VALUES ('Nemis tili')"
# )

# cur.execute(
#     "INSERT INTO enrolments (student_id,course_id) VALUES (1,1),(1,2),(2,1),(2,3),(3,1)"
# )