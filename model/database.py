import configparser
import pymysql


class Database():
    """
    Class responsible for connection with mysql database

    """
    def __init__(self):
        cp = configparser.ConfigParser()
        cp.read("database.ini")
        self.db_name = cp['database']['db_name']
        self.user = cp['database']['user']
        self.password = cp['database']['password']
        self.host = cp['database']['host']
        self.connection = False
        self.cursor = False

    def connect(self):
        if self.connection == False and self.cursor == False:
            self.connection = pymysql.connect(host=self.host, user=self.user, passwd=self.password, db='mysql', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection != False and self.cursor != False:
            self.cursor.close()
            self.connection.close()
            self.connection = False
            self.cursor = False

    def execute(self, sql):
        self.connect()
        self.cursor.execute(sql)
        if "INSERT" in sql:
            result = self.cursor.lastrowid
        else:
            result = self.cursor.fetchall()
        self.connection.commit()
        self.disconnect()
        return result