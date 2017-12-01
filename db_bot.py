import sqlite3


class DbBot:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS lives (description text, name_username text, votes int)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, item_text, username):
        stmt = "INSERT INTO lives (description, name_username, votes) VALUES (?, ?, ?)"
        args = (item_text, username, 0)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM lives WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_lives(self):
        stmt = "SELECT description FROM lives"
        return [x[0] for x in self.conn.execute(stmt)]

    def get_lives_from(self):
        stmt = "SELECT description, name_username FROM lives"
        return [[x[0], x[1]] for x in self.conn.execute(stmt)]

    def get_lives_list(self):
        stmt = "SELECT description, name_username, votes FROM lives"
        return [[x[0], x[1], x[2]] for x in self.conn.execute(stmt)]

    def len_votes(self, live_description):
        stmt = "SELECT votes FROM lives WHERE description = (?)"
        args = (live_description, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def update_votes(self, chosen_live, add_vote):
        stmt = "UPDATE lives SET votes = (?) WHERE description = (?)"
        args = (add_vote, chosen_live)
        self.conn.execute(stmt, args)
        self.conn.commit()


        # **** self.conn.close() ****