const socketio = io.connect("http://192.168.7.153:5000")

const sendBtn = document.querySelector("button")

sendBtn.addEventListener('click', ()=> {
    const message = document.getElementById("message")

    socketio.emit('recieve msg', {message: message.value})
})

socketio.on("send message", (msg) => {
    const content = document.querySelector(".chat-content")
    const div = document.createElement("div")
    div.classList.add("box3", "sb14")
    div.textContent = `${msg.name}: ${msg.message}`

    content.appendChild(div)
    var scrollBar = document.getElementById('scroll');
    scrollBar.scrollTop = scrollBar.scrollHeight;
})




