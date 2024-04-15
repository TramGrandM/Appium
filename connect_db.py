import psycopg2


def connect(query):
    conn = psycopg2.connect(
        user="genki_dev",
        password="genkipw123456",
        database="genki",
        host="stg-db.genkimiru.jp",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows
