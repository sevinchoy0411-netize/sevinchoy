from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE company"
# )
# print("Database succesfully created")

# cur.execute(
    # """
    # CREATE TABLE worker(
    # id SERIAL PRIMARY KEY,
    # name VARCHAR(100),
    # duty VARCHAR(100)
    # )
    # """
# )
# print("Table created succesfully")

# cur.execute(
    # """
    # CREATE TABLE company(
    # id SERIAL PRIMARY KEY,
    # title VARCHAR(100)
    # )
    # """
# )
# print("Table created succesfully")

# cur.execute(
    # """
    # CREATE TABLE staff(
    # id SERIAL PRIMARY KEY,
    # worker_id INTEGER,
    # company_id INTEGER
    # )
    # """
# )
# print("Table created succesfully")

# cur.execute(
    # "INSERT INTO worker (name,duty) VALUES ('Sevinchoy','director/cybersecurity officer')"
# )

# cur.execute(
    # "INSERT INTO company (title) VALUES ('CyberNest')"
# )

# cur.execute(
    # "INSERT INTO staff (worker_id,company_id) VALUES (1,1)"
# )

# cur.execute(
#     "SELECT worker.name,company.title,worker.duty FROM staff JOIN worker ON worker.id=staff.worker_id JOIN company ON company.id=staff.company_id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)