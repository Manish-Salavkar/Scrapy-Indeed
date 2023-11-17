# job\job\database_manager.py
import psycopg2
from scrapy.utils.project import get_project_settings

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def get_connection(self):
        if not self.connection:
            settings = get_project_settings()
            db_config = settings.get('DATABASE_CONFIG', {})
            self.connection = psycopg2.connect(
                database=db_config.get('database', 'database'),
                user=db_config.get('user', 'user'),
                password=db_config.get('password', 'password'),
                host=db_config.get('host', 'localhost'),
                port=db_config.get('port', 'port')
            )
        if not self.cursor:
            self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.cursor = None
            self.connection = None

database_manager = DatabaseManager()
