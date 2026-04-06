import psycopg2
def db_connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "learning_center",
        user = "postgres",
        password = "04112012"
    )
    return conn