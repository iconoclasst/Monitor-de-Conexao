import sqlite3
import time
from capture import get_connections

def insert(cursor, c):
    cursor.execute("INSERT INTO connections (lip, lport, rip, rport, proto) VALUES (?, ?, ?, ?, ?)", c)
    
def main():
    con = sqlite3.connect("connections.db")
    cursor = con.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS connections(id INTEGER PRIMARY KEY AUTOINCREMENT, lip TEXT NOT NULL, lport INTEGER NOT NULL, rip TEXT NOT NULL, rport INTEGER NOT NULL, proto TEXT NOT NULL)")

    seen = set()

    try:
        while True:
            for c in get_connections():
                if c not in seen:
                    insert(cursor, c)
                    seen.add(c)
            con.commit()
            time.sleep(1)
    except KeyboardInterrupt:
        con.close()
