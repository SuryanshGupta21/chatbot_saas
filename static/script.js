function sendMessage() {
    let userInput = document.getElementById("userInput").value;
    let chatbox = document.getElementById("chatbox");

    chatbox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    document.getElementById("userInput").value = "";

    fetch("https://chatbot-saas.onrender.com", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
            chatbox.scrollTop = chatbox.scrollHeight;
        })
        .catch(error => console.error("Error:", error));
}
