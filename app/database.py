import sqlite3, os

class Database:
    def __init__(self) -> None:
        self.dbdir = f'{os.getcwd()}/resources/accounts.db'
        self.init_db()

        self.conn = sqlite3.connect(self.dbdir)


    def init_db(self):
        if not os.path.exists(self.dbdir):
            f = open(self.dbdir, "x")
            f.close()

    def login(username, password):

        return True
    
    def register(username, password):

        return True