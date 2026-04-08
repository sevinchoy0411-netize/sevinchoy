from db import db_connect

con = db_connect()
con.autocommit = True
cur = con.cursor()

# cur.execute(
    # "CREATE DATABASE library"
# )
# print("Database created")

# cur.execute(
#     """
#     CREATE TABLE readers(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE books(
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE renters(
#     reader_id INTEGER,
#     book_id INTEGER
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO readers (name) VALUES ('Rayhona')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO books (title) VALUES ('Yulduzlar mangu yonadi')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO renters (reader_id,book_id) VALUES (1,5),(2,1),(3,4)"
# )
# print("Succesfully added")

cur.execute(
    "SELECT readers.name , books.title FROM renters JOIN readers ON readers.id = renters.reader_id JOIN books ON books.id = renters.book_id"
)
rows = cur.fetchall()
for row in rows:
    print(row)