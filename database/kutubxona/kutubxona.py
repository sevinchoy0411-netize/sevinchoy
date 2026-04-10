from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE kutubxona"
# )

# cur.execute(
#     """
#     CREATE TABLE authors(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )

# cur.execute(
#     """
#     CREATE TABLE books(
#     id SERIAL PRIMARY KEY,
#     book_name VARCHAR(100)
#     )
#     """
# )

# cur.execute(
#     "INSERT INTO books (book_name) VALUES ('Sen bir olam men ozga olam')"
# )

cur.execute(
    "SELECT authors.name , books.book_name FROM authors LEFT JOIN books ON authors.id = books.id"
)
rows = cur.fetchall()
for row in rows:
    print(row)