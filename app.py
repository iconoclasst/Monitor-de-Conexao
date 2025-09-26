from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB = "connections.db"

@app.route("/connections")
def connections():
    con = sqlite3.connect(DB)
    cursor = con.cursor()
    cursor.execute(
        "SELECT id, lip, lport, rip, rport, proto FROM connections ORDER BY id DESC LIMIT 10"
    )
    rows = cursor.fetchall()
    con.close()
    result = [{"id": r[0], "local_ip": r[1], "local_port": r[2], "remote_ip": r[3], "remote_port": r[4], "proto": r[5]} for r in rows ]

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
