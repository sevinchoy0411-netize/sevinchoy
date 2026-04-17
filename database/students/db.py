import psycopg2
def connect_db():
    conn = psycopg2.connect(
        host = "localhost",
        database = "students",
        user = "postgres",
        password = "04112012"
    )
    return conn