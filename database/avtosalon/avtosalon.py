from connect_db import db_conect

conn = db_conect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE avtosalon"
# )
# print("Database created")

# cur.execute(
    # """
    # CREATE TABLE customer(
    # id SERIAL PRIMARY KEY,
    # name VARCHAR(100)
    # )
    # """
# )
# print("Table created")

# cur.execute(
    # """
    # CREATE TABLE cars(
    # id SERIAL PRIMARY KEY,
    # model VARCHAR(100)
    # )
    # """
# )
# print("Table created")

# cur.execute(
    # """
    # CREATE TABLE enrollments(
    # customer_id INTEGER,
    # car_id INTEGER
    # )
    # """
# )
# print("Table created")

# cur.execute(
    # "UPDATE customer SET name='Sevinchoy' WHERE id=3"
# )

# cur.execute(
    # "INSERT INTO cars (model) VALUES ('BMW')"
# )

# cur.execute(
    # "INSERT INTO enrollments (customer_id,car_id) VALUES (1,3),(2,1),(3,2)"
# )

# cur.execute(
#     "SELECT customer.name , cars.model FROM enrollments JOIN customer ON customer.id = enrollments.customer_id JOIN cars ON cars.id = enrollments.car_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)