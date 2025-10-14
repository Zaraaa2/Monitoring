import pymysql
from app import config

def get_active_users():
    try:
        conn = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database=config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cur:
            cur.execute("SELECT username, acctstarttime, framedipaddress FROM radacct WHERE acctstoptime IS NULL LIMIT 10;")
            return {"active_users": cur.fetchall()}
    except Exception as e:
        return {"error": str(e)}
