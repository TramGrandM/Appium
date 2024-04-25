import time

import psycopg2


def connect(query):
    conn = psycopg2.connect(
        user="prod_tester",
        password="UWuxJ9vrOWuH",
        database="genki",
        host="db2.genkimiru.jp",
        port="5432"
    )
    cur = conn.cursor()
    time.sleep(5)
    cur.execute(query)
    rows = cur.fetchall()
    return rows
