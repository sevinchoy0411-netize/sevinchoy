import psycopg2
def db_connect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "vorislar",
        user = "postgres",
        password = "04112012"
    )