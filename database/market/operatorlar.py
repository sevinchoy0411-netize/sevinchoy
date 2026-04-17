from db import connect

conn = connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
#     "SELECT * FROM products WHERE price <= 10000"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM products WHERE price >= 10000"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "SELECT * FROM products WHERE price != 10000"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)


cur.execute(
    "SELECT * FROM products WHERE price <> 10000"
)
rows = cur.fetchall()
for row in rows:
    print(row)