from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

cur.execute(
    "SELECT * FROM products ORDER BY name"
)
rows = cur.fetchall()
for row in rows:
    print(row)