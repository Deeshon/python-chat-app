const socketio = io.connect("http://192.168.7.153:5000")

const sendBtn = document.querySelector("button")

sendBtn.addEventListener('click', ()=> {
    const username = document.getElementById("username")
    const message = document.getElementById("message")

    socketio.emit('recieve msg', {username: username.value, message: message.value})
})

socketio.on("send message", (msg) => {
    const content = document.querySelector(".content")
    const p = document.createElement("p")
    p.textContent = `${msg.username}: ${msg.message}`

    content.appendChild(p)
})


