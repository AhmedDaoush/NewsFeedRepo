from os import environ
from pymysql import connect, cursors


def get_db_connection():
    return connect(
        host=environ.get("DB_HOST"),
        port=int(environ.get("DB_PORT")),
        database=environ.get("DB_NAME"),
        user=environ.get("DB_USER"),
        password=environ.get("DB_PASSWORD"),
        cursorclass=cursors.DictCursor
    )
