from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time
from datetime import datetime

from prompt import SYSTEM_PROMPT as ZERO_SHOT_PROMPT
from fewshot_prompt import SYSTEM_PROMPT as FEW_SHOT_PROMPT

# ==========================================
# Load Environment Variables
# ==========================================
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ==========================================
# Header
# ==========================================
print("\n" + "=" * 65)
print("🤖 LLM INFORMATION EXTRACTION USING PROMPT ENGINEERING")
print("=" * 65)

# ==========================================
# Prompt Selection
# ==========================================
print("\nSelect Prompting Technique\n")
print("1. Zero-shot Prompting")
print("2. Few-shot Prompting")

choice = input("\nEnter your choice (1 or 2): ").strip()

if choice == "1":
    SYSTEM_PROMPT = ZERO_SHOT_PROMPT
    prompt_name = "Zero-shot"
elif choice == "2":
    SYSTEM_PROMPT = FEW_SHOT_PROMPT
    prompt_name = "Few-shot"
else:
    print("\n❌ Invalid choice.")
    exit()

print("\n" + "-" * 65)
print(f"✅ Selected Prompt : {prompt_name}")
print("-" * 65)

# ==========================================
# Input File
# ==========================================
filename = input(
    "\nEnter input file name\n"
    "(Example: sample_input.txt or samples/sample1.txt)\n\n> "
).strip()

print("\n📂 Reading input file...")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print(f"\n❌ File '{filename}' not found.")
    exit()

# ==========================================
# Create Prompt
# ==========================================
prompt = f"""
{SYSTEM_PROMPT}

###
{text}
###
"""

print("🤖 Sending prompt to Gemini...")

start_time = time.time()

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0
        )
    )

    end_time = time.time()
    execution_time = round(end_time - start_time, 2)

    # ==========================================
    # Create Output Folder
    # ==========================================
    os.makedirs("outputs", exist_ok=True)

    base_name = os.path.splitext(os.path.basename(filename))[0]
    output_file = f"outputs/{base_name}_output.json"

    print("💾 Saving JSON output...")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(response.text)

    # ==========================================
    # Create Logs Folder
    # ==========================================
    os.makedirs("logs", exist_ok=True)

    with open("logs/extraction_log.txt", "a", encoding="utf-8") as log:

        log.write("\n")
        log.write("=" * 60 + "\n")
        log.write(f"Date : {datetime.now()}\n")
        log.write(f"Prompt : {prompt_name}\n")
        log.write(f"Input File : {filename}\n")
        log.write(f"Output File : {output_file}\n")
        log.write(f"Execution Time : {execution_time} seconds\n")
        log.write("Status : Success\n")
        log.write("=" * 60 + "\n")

    # ==========================================
    # Display Result
    # ==========================================
    print("\n" + "=" * 65)
    print("📄 EXTRACTED INFORMATION")
    print("=" * 65)

    print(response.text)

    print("\n" + "=" * 65)
    print("📊 EXTRACTION SUMMARY")
    print("=" * 65)

    print(f"Prompt Used      : {prompt_name}")
    print(f"Input File       : {filename}")
    print(f"Output File      : {output_file}")
    print(f"Execution Time   : {execution_time} sec")
    print(f"Characters Read  : {len(text)}")
    print(f"Status           : Success")

    print("\n✅ Output saved successfully.")
    print("📝 Log updated successfully.")

except Exception as e:

    print("\n❌ Gemini API is temporarily unavailable.")
    print("Please wait a few minutes and try again.\n")
    print(f"Details:\n{e}")