require('dotenv').config();

const url = 'https://api-sb.bofa.com/cashpro/reporting/v1/transaction-inquiries/current-day';
const ACCOUNT_NAME = '483102030472';
const BANK_ID = '021000322';

// Re-authorize each time
// import retrieve function here
const BOA_BEARER = process.env.BOA_API_KEY;

const data = {
    'fromDate': '2024-05-21',
    'toDate': '2024-05-22',
    'accounts': [
        { accountNumber: ACCOUNT_NAME, bankId: BANK_ID }
    ]
};

fetch(url, {
    method : 'POST',
    headers : {
        'Content-Type' : 'application/json',
        'Authorization' : `Bearer ${BOA_BEARER}`,
    },
    body : JSON.stringify(data),
})
.then(response => {
    if(!response.ok) {
        throw new Error(`\nNetwork response is not ok, response code is ${response.status}: ${response.statusText}`);
    } 
    return response.json();
})
.then(data => {
    console.log(data);
})
.catch(error => {
    console.error('You have an operational error', error)
})