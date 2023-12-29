import psycopg2
from psycopg2.extras import DictCursor


class DBConnectionError(Exception):
    pass


class DB:
    DB_ERROR_YES = True
    DB_ERROR_NO = False

    @classmethod
    def connect(cls, connection_string: str):
        try:
            cls.connection = psycopg2.connect(connection_string)
        except psycopg2.Error as exc:
            raise DBConnectionError() from exc

    @classmethod
    def execute(cls, query: str, values=()):
        try:
            with cls.connection as connection:
                with connection.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query, values)
                return cursor.rowcount, cls.DB_ERROR_NO
        except psycopg2.InterfaceError:
            return 0, cls.DB_ERROR_YES

    @classmethod
    def get_result_one(cls, query: str, values):
        try:
            with cls.connection as connection:
                with connection.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query, values)
                    return cursor.fetchone(), cls.DB_ERROR_NO
        except psycopg2.InterfaceError:
            return 0, cls.DB_ERROR_YES

    @classmethod
    def get_result_all(cls, query):
        try:
            with cls.connection as connection:
                with connection.cursor(cursor_factory=DictCursor) as cursor:
                    cursor.execute(query)
                    return cursor.fetchall(), cls.DB_ERROR_NO
        except psycopg2.InterfaceError:
            return None, cls.DB_ERROR_YES
