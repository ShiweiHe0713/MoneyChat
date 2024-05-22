import os
from openai import OpenAI
from dotenv import load_dotenv
from event_handler import EventHandler

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.create(
    name="MoneyChat",
    instructions=
        """
            You are a personal finance helper to analyze statments, bills and give suggestions.
            You will provide correct answer to the best of your ability.
            You will analyze and validate your responses before you report to the user.
            In the files I provided you with, the postive numbers stand for incoming money, and the
            negative numbers means outgoing money.
        """,
    tools=[{"type": "file_search"}],
    model="gpt-4-turbo-preview",
    tool_resources={"file_search": {"vector_store_ids": ["vs_BAaa7AyNMdawd3TI9wUU3X9j"]}},
)

# Create a thread
thread = client.beta.threads.create()

# `messages`` is an object that has all the messages users sent
# `message` supports both text and files, the number of messages can be added to Thread is unlimited
messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""
        What are the sum of transations listed under "withdrawl and subtraction" from 2024-02-01 to 2024-03-31?
        """,
)

def delete_file_vector_store():
  client.beta.vector_stores.


# Then, we use the `stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Calvin He. The user has a premium account.",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()
