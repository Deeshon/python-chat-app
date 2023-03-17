
const submitBtn = document.querySelector("#submit-btn")

submitBtn.addEventListener('click', (event) => {
    const username = document.getElementById("user-name")
    if (username.value == "") {
        alert("Enter a username")
        event.preventDefault()
    }
})
