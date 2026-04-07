import psycopg2
def db_conect():
    conn = psycopg2.connect(
        host = "localhost",
        database = "avtosalon",
        user = "postgres",
        password = "04112012"
    )
    return conn