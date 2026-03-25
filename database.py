# import psycopg2
# conn = psycopg2.connect(
    # host = "localhost",
    # database = "it_park",
    # user = "postgres",
    # password = "04112012"
# )
# cur = conn.cursor()

# cur.execute(
#     "INSERT INTO pupils (name,age,direction,sinf) VALUES ('Saidabdulla',15,'dasturlash',8)"
# )
# conn.commit()

# cur.execute(
#     "SELECT * FROM pupils"
# )
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.commit()

# cur.execute(
#     "UPDATE pupils SET age=age-1 WHERE id=10"
# )
# conn.commit()

# cur.execute(
#     "DELETE FROM pupils WHERE id=32"
# )
# conn.commit()