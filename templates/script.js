
async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const response = await fetch('http://127.0.0.1:5000/get_openai_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify( { messages: userMessage }),
    });
    if(!response.ok) {
        console.error(`Error occur!`)
    } else {
        const responseData = await response.json();
        const chatBox = document.getElementById('chat-box');
        console.log(responseData)
        chatBox.innerHTML += `<p>User: ${userMessage}</p>`;
        chatBox.innerHTML += `<p>Bot: ${responseData.response}</p>`;
    }
}