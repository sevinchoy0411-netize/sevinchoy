from def_db import db_connect

con = db_connect()
con.autocommit = True
cur = con.cursor()

# cur.execute(
#     "SELECT * FROM students"
# )
# row = cur.fetchall()
# for rows in row:
#     print(rows)
# print("Ma'lumotlar muvaffaqiyatli yuklandi")

# cur.execute(
#     "INSERT INTO students(name,age,subject,sinf) VALUES ('Saddam',14,'backend',8)"
# )
# print("Ma'lumotlar muvaffaqiyatli qo'shildi")