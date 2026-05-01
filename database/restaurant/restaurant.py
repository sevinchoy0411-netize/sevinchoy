from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE restaurant"
# )
# print("Database created")

# cur.execute(
#     """CREATE TABLE chairs(
#     id SERIAL PRIMARY KEY,
#     number INT
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO chairs(number) VALUES(1),(2),(3),(4),(5)"
# )
# print("Added")

# cur.execute(
#     """CREATE TABLE menu(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100),
#     price NUMERIC(10,2)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO menu(name,price) VALUES('Lavash',35000),('Pizza',35000),('Burger',50000),('Shashlik',15000),('Hotdog',15000)"
# )
# print("Added")

# cur.execute(
#     """CREATE TABLE cassa(
#     chair_id INT,
#     food_id INT,
#     total_price NUMERIC(10,2)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO cassa(chair_id,food_id) VALUES(1,2),(1,3),(2,4),(3,1),(4,1),(4,2),(5,2),(5,3)"
# )

cur.execute(
    "SELECT chairs.number,menu.name FROM cassa JOIN chairs ON chairs.id=cassa.chair_id JOIN menu ON menu.id=cassa.food_id"
)
rows = cur.fetchall()
for row in rows:
    print(row)