import psycopg
from config import config
from datetime import datetime


class DBJetson():
    def __init__(self):
        self.conn = None
        self.url = config['DB']['DATABASE_URL']
        self.create_surgeries_table()
    
    def connect(self):
        if self.conn ==None:
            self.conn = psycopg.connect(self.url)
    
    def create_surgeries_table(self):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS "surgery" (
                "id" SERIAL PRIMARY KEY,
                "node_id" INTEGER NOT NULL,
                "category" TEXT NOT NULL,
                "start_time" TIMESTAMP NOT NULL,
                "end_time" TIMESTAMP,
                "bandage" INTEGER NOT NULL,
                "cold_compress" INTEGER NOT NULL,
                "gauze" INTEGER NOT NULL,
                "glove" INTEGER NOT NULL,
                "tape" INTEGER NOT NULL,
                "tweezer" INTEGER NOT NULL
                )""")
            self.conn.commit()

    def update_surgery(self, node_id, item_name):
        self.connect()
        with self.conn.cursor() as cur:
            # cur.execute("""UPDATE surgery SET %s = %s + 1 WHERE node_id = %s;""", (item_name,item_name,node_id))
            cur.execute(f"""UPDATE surgery SET {item_name} = {item_name} + 1 WHERE node_id = {node_id};""")
            self.conn.commit()
