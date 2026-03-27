import psycopg2
def connect_db():
    connect = psycopg2.connect(
    host = "localhost",
    database = "sevinchoy",
    user = "postgres",
    password = "04112012"
    )
    return connect