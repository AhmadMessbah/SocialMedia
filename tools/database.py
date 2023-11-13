import mysql.connector


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3306,
            password="root123",
            database="socialmedia"
        )


        self.cursor = self.connection.cursor()

    def close(self):

        self.cursor.close()
        self.connection.close()

    def execute_sql(self, sql_command, data=None):

        self.cursor.execute(sql_command, data)

        self.connection.commit()

    def fetch_all_results(self, sql_command, data=None):
        self.cursor.execute(sql_command, data)

        results = self.cursor.fetchall()

        return results