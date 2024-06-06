# https://chatgpt.com/c/6a20deaf-cb35-41ce-9aa1-23dd55bde40b
# Finish the code according to the sample code above
import flask
from flask import Flask, jsonify, Response
from typing import List, Dict, Tuple, Any
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
import os

load_dotenv()
app = Flask(__name__)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
message_history = [{'role': 'system', 'content': 'You are a personal finance assistant'}]

@app.route('/')
def home_page():
    return "The flask app is up and running!"

@app.route('/get_openai_response', methods=['GET'])
def get_response() -> Response:
    try:
        # Take the request message send it to chat_bot and get the response return it back to frontend
        data = flask.reqeust.get_json()
        new_message = data.get('message')
        global message_history
        response_content, message_history = chat_bot(new_message, message_history)
        return jsonify({"Response": response_content, "message_history": message_history}), 200
    except Exception as e:
        return jsonify({"Error occur": str(e)}), 500
    
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

if __name__ == "__main__":
    app.run(debug=True)