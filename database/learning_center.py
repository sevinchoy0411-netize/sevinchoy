from db_def import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE learning_center"
# )
# print("Database created")

# cur.execute(
#     """
#     CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
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

