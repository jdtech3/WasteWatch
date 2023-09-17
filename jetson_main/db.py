import psycopg

from config import config

conn = psycopg.connect(config['DB']['DATABASE_URL'])

with conn.cursor() as cur:
    cur.execute("SELECT now()")
    res = cur.fetchall()
    conn.commit()
    print(res)