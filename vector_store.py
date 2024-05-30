import os
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}", 
        "Content-Type": "application/json", 
        "OpenAI-Beta": "assistants=v1",
}

def list_all_files():
    url = "https://api.openai.com/v1/vector_stores/"
    
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        print(json.dumps(data, indent=4))
    except:
        print(response.status_code)

def delete_file_from_vector_store(vector_id):
    url = f"https://api.openai.com/v1/vector_stores/{vector_id}"
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print("Delete successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def delete_all_files_from_vector_store(confirmation):
    if confirmation != "I AM SURE I WANT TO DELETE THEM ALL!":
        return
    url = "https://api.openai.com/v1/vector_stores/"
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        vectors = data["data"]

        for vector in vectors:
            target_url = url + vector["id"]
            try:
                requests.delete(target_url, headers=headers)
            except:
                print(f"Delete {target_url} failed!")
    except:
        print(response.status_code)

def main():
    list_all_files()
    # delete_all_files_from_vector_store("I AM SURE I WANT TO DELETE THEM ALL!")

if __name__ == "__main__":
    main()