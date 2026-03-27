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
#     "INSERT INTO students(name,age,subject,sinf) VALUES ('Humoyun',14,'backend',8)"
# )
# print("Ma'lumotlar muvaffaqiyatli qo'shildi")

# cur.execute(
#     "UPDATE students SET name='Abdumajid' WHERE id=21"
# )
# print("Ma'lumotlar muvaffaqiyatli yangilandi")

