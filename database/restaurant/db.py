import psycopg2
def connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "restaurant",
        user = "postgres",
        password = "04112012"
    )
    return conn