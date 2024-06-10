document.getElementById('userMessage').addEventListener('keypress', (event)=>{
    if (event.key === 'Enter') {
        sendMessage();
    }
});

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

async function uploadFile() {
    const formData = new FormData();
    const fileInput = document.getElementById("userFile");
    formData.append('file', fileInput.files[0]);

    response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
    });

    if(!response.ok) {
        console.error('File upload error!');
    } else {
        const responseDataObject = await response.json();
        
        console.log('File uploaded successfully', responseDataObject);
    }
}

// async function pieChart() {
//     // Month should be retrieved from UI
//     const month = 3;
//     const response = await fetch("http://127.0.0.1:5000/pieChart", {
//         method: 'POST',
//         body: {
//             month: `${month}`
//         },
//     });

//     if(!response.ok) {
//         console.error('Error recieving response from server')
//     } else {
//         // Show the pie chart on the client
//         // Use tablaue or oather BI platform to visual the 
//         const tablaue_object = New Tablue();
//         tablaue_object.data = response.data;
//         tablaue_object.Xaxis = category;
//         tablaue_object.yaxis = expense;
//         tablaue_plot = new tablaue_object.plot();
//         tableu_plot.plot(tablaue_object);
//         return tablaue_plot;
//     }
// }

// async function Trend() {
//     // making request to the server
//     const response = await fetch("http://127.0.0.1:5000/trend", {
//         method: "POST",
//     });

//     if(!response.ok) {
//         console.error("error occur retrieving the trend", error);
//     } else {
//         const tablaue_object = New Tablue();
//         tablaue_object.data = response.data;
//         tablaue_object.Xaxis = month;
//         tablaue_object.yaxis = expense;
//         tablaue_plot = new tablaue_object.plot();
//         tableu_plot.plot(tablaue_object);
//         return tablaue_plot;
//     }
// }