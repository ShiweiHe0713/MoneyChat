import os
from openai import OpenAI
from dotenv import load_dotenv
import boto3

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
session = boto3.Session(
    aws_access_key_id=os.getenv("aws_access_key"),
    aws_secret_access_key = os.getenv("aws_access_secret"),
    region_name="us-east-1"
)

s3_resource = session.resource('s3')


def store_directory(directory = "docs/boa/"):
    vector_store = client.beta.vector_stores.create(name="Financial Statement")
    files = os.listdir(directory)

    # Turn the files into a file stream
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

def store_single_file(path):
    vector_store = client.beta.vector_stores.create(name="Second-Try-Single-File")
    file = open(path, "rb")
    file_ = client.beta.vector_stores.files.upload_and_poll(
        vector_store_id=vector_store.id,
        file=file,
    )
    print(file_)

# store_single_file("docs/expense_data_kaggle.txt")
vector_store_files = client.beta.vector_stores.files.list(
  vector_store_id="vs_6T4ZruLM0TAZi9RucFnSqO4E"
)

print(vector_store_files)