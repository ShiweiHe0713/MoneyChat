const http = require('http')
const express = require('express')
const PORT = process.env.PORT || 3001

const app = express()
const chatBot = require('./chatBot')

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.write('<h1>This is the landing page</h1>');
    res.end();
});

app.get('/chat', (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.write('<h1>This is ChatBot Page</h1>');
    res.end();
});

// Get the latest transaction
app.get('/transactions', (req, res) => {

});

app.use('/', chatBot);

app.listen(PORT, ()=>{
    console.log("The server is listening.");
})
