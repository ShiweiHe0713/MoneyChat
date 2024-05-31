// Transaction requests handling
import { S3Client, ListBucketsCommand, GetObjectCommand } from '@aws-sdk/client-s3';
import express from 'express';
import dotenv from 'dotenv';
import csv from 'csv-parser';
import { PassThrough } from 'stream';

dotenv.config()

const router = express.Router();

const accessKeyIdLocal = process.env.aws_access_key;
const secretAccessKeyLocal = process.env.aws_access_secret;

const s3 = new S3Client({
    region: 'us-east-1',
    credentials: {
        accessKeyId: accessKeyIdLocal,
        secretAccessKey: secretAccessKeyLocal,
    }
});

if (!accessKeyIdLocal || !secretAccessKeyLocal) {
    console.log('Access key or secret not defined!');
    process.exit(1);
}

// Incomplete code
async function uploadFile(bucketName, key, body) {
    try {
        // Sanitize the csv before uploading to S3
        const command = {
            Bucket: bucketName,
            Key: key,
            Body: body
        };
        const response = await s3.send(command);
        console.log('File uploaded successfully: ', response);
    } catch(error) {
        console.error('Error uploading file', error);
    }
};

async function downloadFile(bucketName, key) {
    try {
        const command = GetObjectCommand({
            Bucket: bucketName,
            Key: key
        });
        const response = await s3.send(command);
        console.log('File downloaded successfully: ', response);
    } catch(error) {
        console.error('Error downloading file', error);
    }
}

async function readFile(bucketName, key) {
    try {
        const command = new GetObjectCommand({
            Bucket: bucketName,
            Key: key
        })
        const response = await s3.send(command);
        
        if(response.Body) {
            const passThrough = new PassThrough();
            const result = [];
            response.Body.pipe(passThrough);

            passThrough.pipe(csv({
                cast: true,
                cast_date: true
            }))
                .on('data', (data) => {
                    result.push(data);
                })
                .on('end', () => {
                    // const entries = queryTransactionsOnAmount(result, '100');
                    const entries = queryTransactionsByDate(result, '9/11/2023');
                    console.log('Result entries: ', entries);
                    // console.log("result csv: ", result)
                })
                .on('error', () => {
                    console.error('Error parsing the CSV: ', error);
                })
                return result;
        } else {
            console.log("File is not a readable stream!");
        }
    } catch(error) {
        console.error('Error getting the file from S3: ', error);
    }
}

function queryTransactionsByDate(transactions, date) {
    return transactions.filter(transaction => transaction.Date === date)
}

function queryTransactionsOnAmount(transactions, amount) {
    try {
        return transactions.filter(transaction => transaction.Amount === amount)
    } catch(error) {
        console.error('Can NOT get the transactions: ', error);
    }
}

function main() {
    const bucketName = 'my-aws-bucket-0713';
    const key = 'checking.csv';
    const array = readFile(bucketName, key);
    // queryTransactionsOnDate(array, '2024-03-01');
}

main();

export default router;