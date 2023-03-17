from flask import Flask, render_template, request, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = "secret!"
socketio = SocketIO(app)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        session["name"] = username

        return render_template("chat.html", username=username)
    else:
    
        return render_template("home.html")

@app.route("/chat")
def chat():
    username = session.get("name")
    return render_template("chat.html", username=username)

@socketio.on('recieve msg')
def handle_msg(data, methods=["POST", "GET"]):
    username = session.get("name")
    data["name"] = username
    socketio.emit("send message", data)


if __name__ == "__main__":
    socketio.run(app, host="192.168.7.153", debug=True)