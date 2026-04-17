from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

cur.execute(
    "SELECT * FROM products LIMIT 5"
)
rows = cur.fetchall()
for row in rows:
    print(row)