import psycopg
from config import config
from datetime import datetime


class db_methods():
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
                """CREATE TABLE IF NOT EXIST "surgery" (
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

    def create_surgery(self,node_id,category):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""INSERT INTO surgery(node_id,category,start_time,bandage,cold_compress,gauze,glove,tape,tweezer)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                        (node_id,category,datetime.now(),0,0,0,0,0,0))
            self.conn.commit()

    def update_surgery(self, node_id, item_name):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""UPDATE surgery
                            SET %s = %s +1
                            WHERE node_id = %s;""",
                            (item_name,item_name,node_id))
            self.conn.commit()

    def end_surgery(self,node_id):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""UPDATE surgery
                            SET %s = %s
                            WHERE node_id = %s;""",
                            ('end_time',datetime.now(),node_id))
            self.conn.commit()

    def fetch_category_data(self,category):
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute("""SELECT * FROM surgery
                            WHERE category = %s
                            ORDER BY start_date ASC
                            LIMIT 5""",
                            (category))
            top_5_data = cur.fetchall()
            self.conn.commit()
            cur.execute("""SELECT AVG(bandage),AVG(cold_compress),AVG(gauze),AVG(glove),AVG(tape),AVG(tweezer) FROM surgery; """)
            all_time_average_data = cur.fetchall()
            self.conn.commit()
            return (top_5_data,all_time_average_data)  




