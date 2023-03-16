from flask import Flask, render_template, request, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")

        return render_template("chat.html")
    else:
    
        return render_template("home.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@socketio.on('recieve msg')
def handle_msg(data, methods=["POST", "GET"]):
    socketio.emit("send message", data)


if __name__ == "__main__":
    socketio.run(app, host="192.168.7.153", debug=True)