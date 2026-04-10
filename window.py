import webview
from app import app
import threading

def start_server():
    app.run()

t = threading.Thread(target=start_server)
t.daemon = True
t.start()

webview.create_window("Mi App", "http://127.0.0.1:5000")
webview.start()
