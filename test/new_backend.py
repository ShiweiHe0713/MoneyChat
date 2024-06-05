from openai import OpenAI
from flask import Flask, jsonify
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)
app = Flask(__name__)
client = OpenAI(
    api_key=OPENAI_API_KEY
)

@app.route("/")
def home_page():
    return "Flask app is up and running!"

# Todo: How to keep the app running with the GPT Chat
@app.route("/get_openai_response", methods=['GET'])
def get_data():
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }
    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to retrieve data", "status_code": response.status_code, "response": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def chat_bot(new_message, message_history):
    message_history.append({'role':'user', 'content':new_message})

    stream = client.chat.completions.create(
        model='gpt-4o',
        messages=message_history,
        stream=True
    )

    response_content = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_content += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    
    message_history.append({'role':'system', 'content':response_content})
    return response_content, message_history
    
if __name__ == "__main__":
    app.run(debug=True)
    message_history = [{"role": "system", "content": "You are a helpful assistant."}]
    new_message="Are you good?"
    response, message_history = chat_bot(new_message, [])
    
    for message in message_history:
        print (f'\n{message}\n')