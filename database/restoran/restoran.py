from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE restoran"
# )
# print("Database created")

# cur.execute(
#     """CREATE TABLE orders(
#     id SERIAL PRIMARY KEY,
#     product_name VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO orders(product_name) VALUES('Lavash'),('Burger'),('Pizza'),('Lavash'),('Pizza'),('Burger'),('Hotdog')"
# )
# print("Added")

cur.execute(
    "SELECT COUNT(id), product_name FROM orders GROUP BY product_name"
)
rows = cur.fetchall()
for row in rows:
    print(row)