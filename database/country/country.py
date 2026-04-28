from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE country"
# )
# print("Database created")

# cur.execute(
#     """CREATE TABLE city(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )"""
# )
# print("Table created")

# cur.execute(
#     "INSERT INTO city(name) VALUES('Seoul'),('Hong Kong'),('Darmstadt'),('Berlin'),('London'),('Paris'),('New York'),('TOkio'),('Dubay'),('Rome'),('Munich'),('Hamburg'),('Berlin'),('Cologne'),('Frankfurt'),('Dresden'),('Nuremberg'),('Leipzid'),('Heidelberg'),('Rothenburg'),('Dresden'),('Frankfurt'),('Cologne'),('Darmstadt')"
# )
# print("Added")

cur.execute(
    "SELECT COUNT(id), name FROM city GROUP BY name;"
)
rows = cur.fetchall()
for row in rows:
    print(row)