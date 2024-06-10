# https://chatgpt.com/c/6a20deaf-cb35-41ce-9aa1-23dd55bde40b
# Finish the code according to the sample code above
import os
import flask
from flask_cors import CORS
from flask import Flask, jsonify, request, Response, render_template
from typing import List, Dict, Tuple, Any
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import pandas as pd
import numpy as np
import openpyxl

load_dotenv()
app = Flask(__name__)
CORS(app)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

message_history = [{'role': 'system', 'content': 'You are a personal finance assistant'}]

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get_openai_response', methods=['POST'])
def get_response() -> Response:
    try:
        data = request.get_json()
        new_message = data.get('messages')

        if not new_message:
            return jsonify({'Error': 'No message provided'}), 400
        
        global message_history
        response, message_history = chat_bot(new_message, message_history)
        return jsonify({'response': response, 'message_history': message_history}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def chat_bot(message, message_history):
    """
    Input: str, List[str]
    Output: str, List[str]
    """
    message_history.append({'role': 'user', 'content': message})
    try:
        response = client.chat.completions.create(
            messages=message_history,
            model='gpt-4o',
            stream=True,
        )
        
        response_content = ""
        for chunk in response:
            if chunk and chunk.choices[0].delta.content:
                response_content += chunk.choices[0].delta.content
        message_history.append({'role': 'system', 'content': response_content})

        return response_content, message_history
    except Exception as e:
        print({"error": e}), 500
        raise

@app.route('/upload', methods=['POST'])
def uploadFile():
    try:
        file = request.files['file']
        if file:
            file_path = os.path.join('upload', file.filename)
            file.save(file_path)

            df = pd.read_csv(file_path)

            # convert dataframe to string(csv or json)
            df_string = df.to_csv(index=False)

            message_history[0]["content"] += "Here are the file content of the user's transaction history, and the user is going to ask question about it. "
            message_history[0]["content"] += df_string

            return jsonify({ 'success': f'File ${file.filename} uploaded successfully!' }), 200
        else:
            print("No file uploaded")
            return jsonify({"error": "No file uploaded"}), 400
    except Exception as e:
        return jsonify({ 'Error': f'${e}' }), 500

@app.route('/piechart', methods=['POST'])
def pie_chart():
    # Retrive the file somewhere
    try:
        month = 3
        df = pd.read_csv('upload/checking.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        # Query that month
        df['Month'] = pd.Timestamp()
        monthly_data = df[df['Month'] == 3]
        response = jsonify(monthly_data)
        return response, 200
    except Exception as e:
        return jsonify({ 'Error': f'Error ${e} getting the pie chart' }), 500
  
@app.route('/trend', methods=['Post'])
def trend():
    """Set the default length to the past 6 months"""
    try:
        window = 6
        hash = {}
        # suppose to be a line chart, x-y: month-expense
        # should return a json object containting 6 k-v pairs
        # key is month, value is expenese
        # Have to sum up the each month in a new df
        c = get_month()
        for i in 6:
            cur = df[df['month'] == c - i]
            cur['Total'] = cur['Amount'].sum()
            hash[c-i] = cur['Total']
        return jsonify(hash)
    except Exception as e:
        return jsonify({ 'Error': f'Error ${e} retrieving the trend' }), 500

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         if 'file' not in request.files:
#             return jsonify({'error': 'No file part'}), 400

#         file = request.files['file']

#         if file.filename == '':
#             return jsonify({'error': 'No selected file'}), 400

#         if file:
#             if not os.path.exists('upload'):
#                 os.makedirs('upload')
#             file_path = os.path.join('upload', file.filename)
#             file.save(file_path)
#             print(f'File saved at {file_path}')

#             # Read the file contents if needed
#             with open(file_path, 'r') as f:
#                 file_contents = f.read()
#                 df = pd.read_csv(file_path)
#                 print(df.info())

#             return jsonify({'success': f'File {file.filename} uploaded and read successfully!'}), 200
#         else:
#             print("File doesn't exist")
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
        