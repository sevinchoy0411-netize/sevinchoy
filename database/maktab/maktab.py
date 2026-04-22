from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE itpark"
# )
# print("👌")

# cur.execute(
#     """CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     grade INT,
#     direction VARCHAR(100)
#     )"""
# )
# print("👌")

# cur.execute(
#     "INSERT INTO students(name,grade,direction) VALUES('Maftuna',9,'backend'),('Zoxira',9,'backend'),('Vali',9,'backend'),('Elbek',9,'backend'),('Sulaymon',9,'backend'),('Yoqubboy',9,'backend'),('Ulugbek',9,'backend'),('Sevinchoy',8,'fullstack')"
# )
# print("ok")

# cur.execute(
#     "SELECT * FROM students ORDER BY grade"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE name ILIKE 'M%'"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students LIMIT 4"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT max(grade) FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT min(grade) FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT AVG(grade) FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT SUM(grade) FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT COUNT(id) FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE direction IN ('backend')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE direction NOT IN ('backend')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM students WHERE id BETWEEN 3 AND 5"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT name AS oquvchi_ismi FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)