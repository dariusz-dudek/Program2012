import sqlite3


class Database:
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table, *values):
        self.cursor.execute(f"""CREATE TABLE {table} ({','.join([val for val in values])})""")
        self.connection.commit()

    def insert(self, table, *values):
        self.cursor.execute(f"""INSERT INTO {table} VALUES ({','.join(['?' for _ in values])})""", values)
        self.connection.commit()

    def edit_by_rowid(self, table, field, value, rowid):
        self.cursor.execute(
            f"""UPDATE {table} SET {field}={f"'{value}'" if type(value) == str else value} WHERE rowid={rowid}""")
        self.connection.commit()

    def edit(self, table, field, value, where_field, condition, condition_value):
        self.cursor.execute(
            f"""UPDATE {table} SET {field}={f"'{value}'" if type(value) == str else value} 
            WHERE {where_field} {condition} {f"'{condition_value}'" if type(condition_value) == str else condition_value}""")
        self.connection.commit()

    def delete(self, table, rowid):
        rows_deleted = self.cursor.execute(f"""DELETE FROM {table} WHERE rowid={rowid}""").rowcount
        self.connection.commit()
        return rows_deleted

    def fetch_all(self, table, **conditions):
        return self.cursor.execute(
            f"""SELECT * FROM {table} WHERE {' and '.join([f'{condition}=?' for condition in conditions])}""",
            (conditions.values(),))

    def show_all(self, table, *values):
        self.cursor.execute(f"""SELECT {','.join([val for val in values])} FROM {table}""")
        return self.cursor.fetchall()

    def choice_with_condition(self, table, field, conditions, value):
        self.cursor.execute(f"""SELECT * FROM {table} WHERE {field} {conditions} {value}""")
        return self.cursor.fetchall()
