from connect import db_connect

conn = db_connect()
conn.autocommit = True
cur = conn.cursor()

# cur.execute(
    # "CREATE DATABASE clinic"
# )
# print("Database created")

# cur.execute(
    # """
#     CREATE TABLE patients(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100)
#     )
#     """
# )
# print("Table created")

# cur.execute(
    # """
    # CREATE TABLE doctors(
    # id SERIAL PRIMARY KEY,
    # doc_name VARCHAR(100)
    # )
    # """
# )
# print("Table created")

# cur.execute(
    # """
    # CREATE TABLE clinic(
    # patient_id INTEGER,
    # doc_id INTEGER
    # )
    # """
# )
# print("Table created")

# cur.execute(
    # "INSERT INTO patients (name) VALUES ('Rayhona')"
# )
# print("Patient added")

# cur.execute(
    # "INSERT INTO doctors (doc_name) VALUES ('Kamoladdin')"
# )
# print("Doctor added")

# cur.execute(
    # "INSERT INTO clinic (patient_id,doc_id) VALUES (1,2),(2,1),(3,2),(4,1),(5,2)"
# )
# print("Succes")

# cur.execute(
    # "SELECT patients.name , doctors.doc_name FROM clinic JOIN patients ON patients.id = clinic.patient_id JOIN doctors ON doctors.id = clinic.doc_id"
# )
# rows = cur.fetchall()
# for row in rows:
    # print(row)