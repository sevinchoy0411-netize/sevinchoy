from my_db import connect_db

con = connect_db()
con.autocommit = True
cursor = con.cursor()

# cursor.execute(
#     "CREATE DATABASE sevinchoy"
# )
# print("Database yaratildi")

# cursor.execute(
#     """
#     CREATE TABLE qarindoshlari(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     age INTEGER,
#     connection VARCHAR(100)
#     )
#     """
# )
# print("Jadval yaratildi")

# cursor.execute(
#     "SELECT * FROM qarindoshlari"
# )
# rows = cursor.fetchall()
# print(rows)