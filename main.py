import os
from openai import OpenAI
from dotenv import load_dotenv
from event_handler import EventHandler

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.create(
    name="MoneyChat",
    instructions="You are a personal finance helper to analyze statments, bills and give suggestions",
    tools=[{"type": "file_search"}],
    model="gpt-4-turbo",
)

thread = client.beta.threads.create()

# `messages`` is an object that has all the messages users sent
# `message` supports both text and files, the number of messages can be added to Thread is unlimited
messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me my total expense of last three months",
)

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