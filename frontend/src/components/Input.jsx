export default function Input() {
    // document.getElementById('userMessage').addEventListener('keypress', (event)=>{
    //     if (event.key === 'Enter') {
    //         sendMessage();
    //     }
    // });
    
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
            const chatBot = document.getElementById('chat-box');
            chatBot.innerHTML += `<p>User: ${userMessage} </p>`;
            chatBot.innerHTML += `<p>Bot: ${responseData.response} </p>`;
            document.getElementById('userMessage').value = '';
        }
    }

    return (
        <div>
        <input id="userMessage" placeholder="Please type here"></input>
        <button onClick={sendMessage()}>Send</button>
        </div>
    );
}