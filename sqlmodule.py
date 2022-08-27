import mysql.connector as sqlctr


def connect_server(pw):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pw
        )
        val = 1
    except:
        print("Incorrect Password")
        val = 0
    return connection, pw, val


def connect_database(pw):
    connection = None
    try:
        connection = sqlctr.connect(
            host="localhost",
            user="root",
            password=pw,
            database="Employees_DB"
        )
    except:
        print("Oops! Incorrect Password , Unable To Connect Databse")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()


def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    return res
