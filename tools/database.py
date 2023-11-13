import mysql.connector


class Database:
    def connect(self):
         #self.connection = mysql.connector.connect(
         #    host="localhost",
         #    user="root",
         #    password="root123",
         #   database="socialmedia"
         #)
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            port = 3306,
            password="root123",
            database="socialmedia"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def transaction(self, sql_command, data=None):
        self.connect()
        if data:
            self.cursor.execute(sql_command, data)
        else:
            self.cursor.execute(sql_command)
        self.connection.commit()
        self.disconnect()

    def report(self, sql_command, data=None):
        self.connect()
        if data:
            self.cursor.execute(sql_command, data)
        else:
            self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        self.disconnect()
        return result