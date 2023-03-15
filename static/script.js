
var socketio = io()


const message = document.getElementById("message")
const sendBtn = document.querySelector("#send-btn")
sendBtn.addEventListener("click", () => {
    socketio.emit("message", {data: message.value})
    message.value = ""
})
