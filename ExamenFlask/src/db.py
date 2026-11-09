import mysql.connector

# Ajusta usuario y contraseña a tu MySQL
DB_CONFIG = {
    'host': 'localhost',
    'user': 'Tania',
    'password': 'root',
    'database': 'pizzeria',
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
