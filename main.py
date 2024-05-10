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
    model="gpt-3.5-turbo",
)

# Create a vector store
vector_store = client.beta.vector_stores.create(name="Financial Statement")

# Turn the files into a file stream
directory = "docs/boa/"
files = os.listdir(directory)

file_streams = []
for file in files:
    file_path = os.getcwd() + "/docs/boa/" + file
    if os.path.exists(file_path):
        try:
            file_stream = open(file_path, "rb")
            file_streams.append(file_stream)
        except IOError:
            print(f"Error: Unable to open file '{file}'")
    else:
        print(f"Error: File '{file}' not found")

print("Total files processed:", len(file_streams))

# Use the file batch and poll sdk to upload files
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_streams,
)
# print(file_batch.status, file_batch.file_counts)

# Update the assistant
assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

# Create a thread
thread = client.beta.threads.create()

# `messages`` is an object that has all the messages users sent
# `message` supports both text and files, the number of messages can be added to Thread is unlimited
messages = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is the biggest purchase within the past 3 month, and validate it",
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