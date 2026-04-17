from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE market"
# )
# print("Database created")

# cur.execute(
#     """CREATE TABLE products(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price NUMERIC(10,2)
#     )"""
# )
# print("Table created")

# cur.execute(
    # "INSERT INTO products(name,price) VALUES('olma',10000),('non', 3000), ('sut', 10000), ('guruch', 18000), ('shakar', 14000), ('tuxum', 22000), ('kartoshka', 6000), ('piyoz', 5000), ('sabzi', 4000), ('tovuq goshti', 35000), ('mol goshti', 90000), ('olma', 12000), ('banan', 20000)"
# )
# print("Succesfully added")

cur.execute(
    "SELECT * FROM products"
)
rows = cur.fetchall()
for row in rows:
    print(row)