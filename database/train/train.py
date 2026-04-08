from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE train"
# )
# print("Database created")

# cur.execute(
#     """
#     CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE tickets(
#     id SERIAL PRIMARY KEY,
#     direction VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     """
#     CREATE TABLE booking(
#     user_id INTEGER,
#     ticket_id INTEGER
#     )
#     """
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO users (name) VALUES ('Sevinchoy')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO tickets (direction) VALUES ('xorazm-Buxoro')"
# )
# print("Succesfully added")

# cur.execute(
#     "INSERT INTO booking (user_id,ticket_id) VALUES (1,2),(2,3),(3,1)"
# )
# print("Succesfully added")

cur.execute(
    "SELECT users.name , tickets.direction FROM booking JOIN users ON users.id = booking.user_id JOIN tickets ON tickets.id = booking.ticket_id"
)
rows = cur.fetchall()
for row in rows:
    print(row)