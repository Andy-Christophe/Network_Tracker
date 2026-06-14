import sqlite3

DB_NAME = "network.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS devices (
    mac TEXT PRIMARY KEY,
    ip TEXT,
    vendor TEXT,
    first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
    
    conn.commit()
    conn.close()



def add_device(mac, ip, vendor):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
INSERT OR IGNORE INTO devices (mac, ip, vendor)
    VALUES (?, ?, ?)
""",(mac, ip, vendor))
    
    conn.commit()
    conn.close()



def update_device(mac, ip):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
UPDATE devices
    SET ip = ?, last_seen = CURRENT_TIMESTAMP
    WHERE mac = ?
""",(ip, mac))
    
    conn.commit()
    conn.close()


def device_exists(mac):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT mac FROM devices WHERE mac = ?",(mac,))
    result = cursor.fetchone()

    conn.close()
    return result is not None

def delete_device(mac):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM devices WHERE mac = ?",(mac,))
    
    conn.commit()
    conn.close()

def get_all_devices():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT mac, ip, vendor FROM devices")
    devices = cursor.fetchall()

    conn.close()
    return [{"mac": d[0], "ip": d[1], "vendor": d[2]} for d in devices]
