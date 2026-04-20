import psycopg2
def connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "phoneshop",
        user = "postgres",
        password = "04112012"
    )
    return conn