require('dotenv').config();

const APPLICATION_ID = process.env.APPLICATION_ID;
const CLIENT_ID = process.env.CLIENT_ID;
const CLIENT_SECRET = process.env.CLIENT_SECRET;
const url = "https://api-sb.bofa.com/authn/v1/client-authentication";

data = {
    'applicationID' : APPLICATION_ID,
    'authn' :
        { 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET }
}

fetch(url, {
    method : 'POST',
    headers : {
        'Content-Type' : 'application/json'
    },
    body: JSON.stringify(data),
})
.then(response => {
    if(!response.ok) {
        throw new Error(`Your response is NOT OK! The error code is ${response.status} : ${response.statusText}`)
    }
    return response.json()
})
.then(data => {
    console.log(data);
})
.catch(error => {
    console.error(`You encounter the error ${error}`)
})