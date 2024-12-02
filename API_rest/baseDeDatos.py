import mysql.connector

def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Coco120604@",
            database="bbdd_proyecto",
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        return connection
    except mysql.connector.Error as err:
        raise Exception(f"Error de conexión: {err}")

def get_cursor(connection):
    return connection.cursor()
