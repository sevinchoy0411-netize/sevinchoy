from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE phoneshop"
# )

# cur.execute(
#     """CREATE TABLE phones(
#     id SERIAL PRIMARY KEY,
#     brand VARCHAR(80),
#     model VARCHAR(100),
#     price NUMERIC(10,2)
#     )"""
# )

# cur.execute(
#     "INSERT INTO phones(brand,model,price) VALUES('Samsung','A36',5000000),('Samsung','S24',12000000),('iPhone','17',18000000),('iPhone','17 AIR',1600000)"
# )

# cur.execute(
#     "SELECT max(price) FROM phones"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT min(price) FROM phones"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)


# cur.execute(
#     "SELECT AVG(price) FROM phones"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT COUNT(id) FROM phones"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT SUM(price) FROM phones"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM phones WHERE brand IN ('Samsung')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM phones WHERE brand NOT IN ('Samsung')"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)