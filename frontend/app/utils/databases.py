import logging
from typing import Any
import psycopg2
from psycopg2 import OperationalError

class TimescaleInterface:
    _instance = None

    @classmethod
    def instance(cls) -> Any:
        if cls._instance is None:
            try:
                cls._instance = TimescaleInterface()
            except OperationalError as e:
                logging.error("Unable to connect to database.")
                logging.error(e)
                return None
        return cls._instance

    def __init__(self, db_name='contacts', db_user='test_user', db_password='test_pass', db_host='database', dp_port=5432) -> None:
        if self._instance is not None:
            raise RuntimeError("Do not instantiate this interface. Use class instance method.")
        self._conn = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=dp_port
        )
        self._conn.autocommit = True

    def execute_query(self, query: str) -> bool:
        cursor = self._conn.cursor()
        return self._db_query_wrapper(cursor.execute, query)
    
    def insert_records(self, query, values) -> bool:
        cursor = self._conn.cursor()
        return self._db_query_wrapper(cursor.executemany, query, values)

    def get_records(self, query) -> Any:
        cursor = self._conn.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except OperationalError as err:
            logging.error(err)
            return None
    
    def _db_query_wrapper(self, action, *args, **kwargs) -> bool:
        try:
            action(*args, **kwargs)
        except OperationalError as err:
            logging.error(err)
            return False
        return True


