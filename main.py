import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.create(
    name="MoneyChat",
    instructions="You are a personal finance helper to analyze statments, bills and give suggestions",
    tools=[{"type": "file_search"}],
    model="gpt-4-turbo",
)

