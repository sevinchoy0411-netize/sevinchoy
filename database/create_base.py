# import psycopg2
# conn = psycopg2.connect(
#     host = "localhost",
#     database = "vorislar",
#     user = "postgres",
#     password = "04112012"
# )
# conn.autocommit = True
# cur = conn.cursor()

# cur.execute(
#     "CREATE DATABASE vorislar"
# )
# print("Database yaratildi")

# cur.execute(
#     """
#     CREATE TABLE students(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR,
#     age INTEGER,
#     subject VARCHAR,
#     sinf INTEGER
#     )
#     """
# )
# print("Jadval yaratildi")