from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

## load the Groq API key
os.environ['NVIDIA_API_KEY'] = os.getenv("NVIDIA_API_KEY")


client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = ""
)

completion = client.chat.completions.create(
  model="mistralai/mixtral-8x22b-instruct-v0.1",
  messages=[{"role":"user","content":"Write a blog about Inferencing of GenAI model in Nvidia."}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

