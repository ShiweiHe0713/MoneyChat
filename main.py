import os
from openai import OpenAI
from dotenv import load_dotenv
from event_handler import EventHandler

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
vector_store_id = "vs_xUvURyFMrSt4jMpu4gQ0ckmj"

assistant = client.beta.assistants.create(
    name="MoneyChat2",
    instructions=
        """
            You are a personal finance helper to analyze statments, bills and give suggestions.
            You will provide correct answer to the best of your ability.
            You will analyze and validate your responses before you report to the user.
            In the files I provided you with, the postive numbers stand for incoming money, and the
            negative numbers means outgoing money.
        """,
    tools=[{"type": "file_search"}],
    model="gpt-4o",
    tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
)

# Create a thread
thread = client.beta.threads.create()

# `messages`` is an object that has all the messages users sent
# `message` supports both text and files, the number of messages can be added to Thread is unlimited
messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""
        
        """,
)
# Then, we use the `stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
stream = client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Calvin He. The user has a premium account.",
  event_handler=EventHandler()
)

if stream is None:
    print("The stream is None")
else:
    with stream as s:
        s.until_done()
