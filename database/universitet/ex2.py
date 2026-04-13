from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

cur.execute(
    "SELECT talabalar.name , kurslar.name FROM talabalar LEFT JOIN kurslar ON talabalar.id = kurslar.id"
)
rows = cur.fetchall()
for row in rows:
    print(row)