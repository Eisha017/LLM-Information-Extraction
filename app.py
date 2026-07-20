from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

from fewshot_prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("sample_input.txt", "r") as file:
    text = file.read()

prompt = f"""
{SYSTEM_PROMPT}

###
{text}
###
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0
    )
)

print(response.text)

with open("output.json", "w") as file:
    file.write(response.text)

print("\n✅ Output saved to output.json")