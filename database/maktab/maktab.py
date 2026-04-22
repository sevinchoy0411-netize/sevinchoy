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

# cur.execute(
#     "SELECT * FROM students"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)