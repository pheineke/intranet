import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data/users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_user_table()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def authenticate_user(self, username, password):
        self.cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        row = self.cursor.fetchone()
        if row and row[0] == password:
            return True
        return False

    def register_user(self, username, password):
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def close(self):
        self.conn.close()
