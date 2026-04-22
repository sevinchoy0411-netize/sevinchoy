from db import db_connect

conn  = db_connect()
cur = conn.cursor()
conn.autocommit = True

# cur.execute(
#     "CREATE DATABASE book_shop"
# )
# print("Create database")

# cur.execute(
#     """
#     CREATE TABLE books (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR,
#     author VARCHAR(80),
#     ganre VARCHAR(80),
#     language VARCHAR(80),
#     pages INTEGER,
#     price NUMERIC(10,2)
#     )

#     """
# )
# print("Create table")

# cur.execute(
#     "INSERT INTO books (name, author, ganre, language, pages, price) VALUES ('Otkan kunlar', 'Abdulla Qodiriy', 'Roman', 'Uzbek', 320, 45000), ('Mehrobdan chayon', 'Abdulla Qodiriy', 'Roman', 'Uzbek', 280, 40000), ('Ikki eshik orasi', 'Otkir Hoshimov', 'Roman', 'Uzbek', 350, 50000), ('Dunyoning ishlari', 'Otkir Hoshimov', 'Qissa', 'Uzbek', 200, 35000), ('Shum bola', 'Gafur Gulom', 'Qissa', 'Uzbek', 150, 30000), ('Alkimyogar', 'Paulo Coelho', 'Falsafa', 'Uzbek', 200, 38000), ('1984', 'George Orwell', 'Distopiya', 'English', 328, 55000), ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 'English', 180, 47000), ('To Kill a Mockingbird', 'Harper Lee', 'Classic', 'English', 281, 52000), ('Atomic Habits', 'James Clear', 'Self-help', 'English', 320, 60000)"
# )
# print("added")

# cur.execute(
#     "SELECT * FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books ORDER BY name"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books WHERE name ILIKE 'T%'"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books LIMIT 5"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT max(price) FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT min(price) FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT AVG(price) FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT SUM(price) FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT COUNT(id) FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books WHERE language IN ('Uzbek')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books WHERE language NOT IN ('Uzbek')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM books WHERE price BETWEEN 30000 AND 50000"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT name AS kitob_nomi FROM books"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)