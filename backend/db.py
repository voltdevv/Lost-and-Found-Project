import sqlite3

class Database:

    def __init__(self):
        self.con = sqlite3.connect('Lost_and_Found.db')
        self.cursor = self.con.cursor()


    