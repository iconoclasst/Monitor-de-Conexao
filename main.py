import threading
import conn
import app

def run_conn():
    conn.main()

def run_app():
    app.app.run(debug=False, use_reloader=False)

if __name__ == "__main__":

    t1 = threading.Thread(target=run_conn)
    t2 = threading.Thread(target=run_app)

    t1.start()
    t2.start()

    t1.join()
    t2.join()