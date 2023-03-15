from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def home():
    return render_template("home.html")

@socketio.on('recieve msg')
def handle_msg(data, methods=["POST", "GET"]):
    socketio.emit("send message", data)


if __name__ == "__main__":
    socketio.run(app, host="192.168.1.22", debug=True)