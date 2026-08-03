async function send() {
    const message = document.getElementById("message").value;

    if (!message.trim()) {
        return;
    }

    document.getElementById("reply").textContent = "Thinking...";

    try {
        const res = await fetch("https://jarvisx-0lag.onrender.com/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await res.json();
        document.getElementById("reply").textContent = data.reply;
    } catch (err) {
        document.getElementById("reply").textContent =
            "Error: " + err.message;
    }
}

