from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE shop"
# )
# print("ok")

# cur.execute(
#     """CREATE TABLE products(
#     id SERIAL PRIMARY KEY,
#     brand VARCHAR(100),
#     model VARCHAR(100),
#     price NUMERIC(10,2)
#     )"""
# )
# print("ok")

# cur.execute(
#     "INSERT INTO products(brand,model,price) VALUES('Artel','TV 90',1500000),('Artel','Muzlatgich 100L',10000000),('Samsung','Galaxy S26',16000000),('Samsung','Changyutkich',1000000)"
# )
# print("ok")

# cur.execute(
#     "SELECT min(price) FROM products"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT max(price) FROM products"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT AVG(price) FROM products"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT SUM(price) FROM products"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT COUNT(id) FROM products"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM products WHERE brand IN ('Artel')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM products WHERE brand NOT IN ('Artel')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)