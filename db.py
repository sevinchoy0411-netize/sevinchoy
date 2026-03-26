import psycopg2
con = psycopg2.connect(
    host = "localhost",
    database = "vorislar",
    user = "postgres",
    password = "04112012"
)
con.autocommit = True
cur = con.cursor()

cur.execute(
    "INSERT INTO students (name,age,subject,sinf) VALUES('',14,'backend',8)"
)

# cur.execute(
#     "SELECT * FROM users"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute(
#     "UPDATE users SET age=age-1 WHERE id=4"
# )

# cur.execute(
#     "DELETE FROM users WHERE id=1"
# )