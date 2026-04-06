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

# cur.execute(
    # "INSERT INTO students (name) VALUES ('Valijon')"
# )
# print("Student added")

# cur.execute(
    # "UPDATE students SET name='Zoxira' WHERE id=2"
# )

# cur.execute(
    # "INSERT INTO courses (title) VALUES('Kompyuter savodxonligi')"
# )
# print("Course added")

# cur.execute(
#     "SELECT * FROM enrolments"
# )
# rows = cur.fetchall()
# print(rows)

# cur.execute(
    # "INSERT INTO enrolments (student_id,course_id) VALUES (2,1)"
# )

# cur.execute(
#     "SELECT students.name,courses.title FROM enrolments JOIN students ON students.id=enrolments.student_id JOIN courses ON courses.id=enrolments.course_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)