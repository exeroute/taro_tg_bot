import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def user_exists(self, chat_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'manager' WHERE 'chat_id' = ?", (chat_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, chat_id, username):
        with self.connection:
            return self.cursor.execute("INSERT OR IGNORE INTO 'manager' ('chat_id', 'username') VALUES (?, ?)",
                                       (chat_id, username))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT chat_id FROM manager").fetchall()

    def get_rubles(self):
        with self.connection:
            return self.cursor.execute("SELECT rubles FROM manager").fetchall()

    #gpt
    def get_rubs(self, chat_id):
        with self.connection:
            return self.cursor.execute("SELECT rubles FROM manager WHERE chat_id = ?", (chat_id,)).fetchone()
