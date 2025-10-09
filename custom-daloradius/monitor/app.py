import os, time, pymysql, subprocess

db = pymysql.connect(
    host=os.getenv('DB_HOST', 'db'),
    user=os.getenv('DB_USER', 'radius'),
    password=os.getenv('DB_PASS', 'radiuspassword'),
    database=os.getenv('DB_NAME', 'radius')
)

def check_nas(host):
    try:
        output = subprocess.check_output(['snmpget', '-v2c', '-c', 'public', host, '1.3.6.1.2.1.1.3.0'], stderr=subprocess.DEVNULL)
        return True if output else False
    except subprocess.CalledProcessError:
        return False

while True:
    cursor = db.cursor()
    cursor.execute("SELECT nasname FROM nas")
    for (nasname,) in cursor.fetchall():
        status = 'up' if check_nas(nasname) else 'down'
        cursor.execute("INSERT INTO nas_status (nasname, status) VALUES (%s,%s) ON DUPLICATE KEY UPDATE status=%s, last_check=NOW()", (nasname, status, status))
        db.commit()
    cursor.close()
    time.sleep(int(os.getenv('CHECK_INTERVAL', 30)))
