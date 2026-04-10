from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE kompaniya"
# )

# cur.execute(
#     """
#     CREATE TABLE worker(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )


# cur.execute(
#     """
#     CREATE TABLE job(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )

# cur.execute(
#     "INSERT INTO job (name) VALUES ('Dizayner')"
# )

# cur.execute(
#     "SELECT worker.name , job.name FROM worker LEFT JOIN job ON worker.id = job.id"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)