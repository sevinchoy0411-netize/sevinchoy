from db import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

cur.execute(
    "SELECT talabalar.name , kurslar.name FROM enrolments JOIN talabalar ON talabalar.id = enrolments.student_id JOIN kurslar ON kurslar.id = enrolments.course_id"
)
rows = cur.fetchall()
for row in rows:
    print(row)