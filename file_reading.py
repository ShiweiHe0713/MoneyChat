import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

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
print(file_batch.status, file_batch.file_counts)
