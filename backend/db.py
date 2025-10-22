import sqlite3

class Database:

    def __init__(self, db_name):
        self.con = sqlite3.connect(f'{db_name}.db')
        self.cursor = self.con.cursor()

    def setup(self, table_name, *values):
        vals = ", ".join(values)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({vals})")
        self.con.commit()

    def add_item(self, table_name, *values):
        vals = ', '.join(values)
        for val in values:
            placeholders += ", ".join('?')
        query = f"INSERT INTO {table_name}, ({vals}) VALUES ({placeholders})"
        

    def fetch_all(self, table_name):

        self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()



    