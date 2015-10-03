import sqlite3

__author__ = 'marcelo_garay'
import os


class DBManager(object):
    db_name = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../../db/sicarios'))

    def __init__(self):
        """
        Make connection to an SQLite database file
        :param db:
        :return:
        """
        self.conn = sqlite3.connect(self.db_name)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def query(self, arg):
        """
        Execute a query using the arg
        :return
        """
        self.cur.execute(arg)
        self.conn.commit()
        return self.cur

    def close(self):
        """
        Close connection to the database
        """
        self.conn.close()
