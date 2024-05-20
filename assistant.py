import os
import time
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
print(f"API Key: {api_key}")

client = OpenAI(api_key=api_key)

# Function to create assistant
def create_assistant(client):
    return client.beta.assistants.create(
        name="Fitness Assistant",
        instructions="You are a personal fitness coach. Write meal plans for meals 3 times a day each day of the week with recipes and excercise routines for meeting the clients target weight and body goals. Emphasise diet over cardio for wright loss. Make sure client hits protein requirmwnt of 1.2g of protein per kg of body weight per day for muscle building of needed. Share macros and calories of each meal as well.",
        model="gpt-3.5-turbo-0125",
    )

# Function to create thread
def create_thread(client):
    return client.beta.threads.create()

# Function to create message
def create_message(client, thread_id):
    return client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content="I am a 85 kg male. I want to get to 80kg in two months and maintain muscle. Give me a plan"
    )

# Function to create and poll run with retries
def create_and_poll_run_with_retries(client, thread_id, assistant_id, instructions, retries=3, delay=5):
    for attempt in range(retries):
        try:
            run = client.beta.threads.runs.create_and_poll(
                thread_id=thread_id,
                assistant_id=assistant_id,
                instructions=instructions
            )
            return run
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

assistant = create_assistant(client)
print("Assistant created successfully.")

thread = create_thread(client)
print("Thread created successfully.")

message = create_message(client, thread.id)
print("Message created successfully.")

run = create_and_poll_run_with_retries(
    client,
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions=assistant.instructions
)
print("Run created and polling started.")

# Wait for the run to complete and get the response
try:
    while run.status not in ["completed", "failed"]:
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        print(f"Run status: {run.status}")

    if run.status == "completed":
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        for msg in messages:
            print(msg.content)
    elif run.status == "failed":
        print("Run failed.")
        error_details = run.last_error
        print(f"Error details: {error_details}")
except Exception as e:
    print(f"Error during run polling or message retrieval: {e}")
