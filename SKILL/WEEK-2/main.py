
import os
import ollama
from dotenv import load_dotenv

# Step 1: Load environment variables
load_dotenv()

# Step 2: Read Ollama configuration
model = os.getenv("OLLAMA_MODEL")
host = os.getenv("OLLAMA_HOST")

if not model or not host:
    raise ValueError("Ollama configuration not found in .env!")

# Step 3: Initialize Ollama client
client = ollama.Client(host=host)

# Step 4: Make first LLM call
response = client.chat(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is Artificial Intelligence? Explain in simple words."
        }
    ]
)

# Step 5: Display response
print("\nOllama Response:")
print(response["message"]["content"])
