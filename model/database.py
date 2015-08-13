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
            self.connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
            self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection != False and self.cursor != False:
            self.cursor.close()
            self.connection.close()
            self.connection = False
            self.cursor = False

    def execute(self, sql):
        self.connect()
        result = self.cursor.execute(sql)
        self.disconnect()
        return result