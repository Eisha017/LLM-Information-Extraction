# 🤖 LLM Information Extraction using Prompt Engineering

A Python application that extracts structured information from unstructured text using Google's Gemini Large Language Model (LLM).

This project demonstrates Prompt Engineering techniques including Zero-shot Prompting, Few-shot Prompting, Delimiters, and Deterministic Generation (Temperature = 0).

---

## 📌 Features

- Zero-shot Prompting
- Few-shot Prompting
- Delimiters for clear prompt structure
- Deterministic JSON generation (Temperature = 0)
- Extracts:
  - Name
  - Company
  - Job Title
  - Email
  - Phone Number
- Supports multiple input files
- Saves output as JSON

---

## 🛠️ Tech Stack

- Python 3
- Google Gemini API
- Prompt Engineering
- python-dotenv

---

## 📂 Project Structure

```text
LLM-Information-Extraction/
│
├── app.py
├── prompt.py
├── fewshot_prompt.py
├── sample_input.txt
├── output.json
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── samples/
│   ├── sample1.txt
│   ├── sample2.txt
│   ├── sample3.txt
│   ├── sample4.txt
│   └── sample5.txt
│
├── outputs/
│
└── docs/
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Eisha017/LLM-Information-Extraction.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### 4. Run the project

```bash
python app.py
```

Enter any sample file when prompted.

Example:

```
samples/sample1.txt
```

---

## 📥 Example Input

```
Hello,

My name is Sarah Johnson.

I work as a Software Engineer at Google.

Email:
sarah@gmail.com

Phone:
+1 555-111-2233
```

---

## 📤 Example Output

```json
{
    "name": "Sarah Johnson",
    "company": "Google",
    "job_title": "Software Engineer",
    "email": "sarah@gmail.com",
    "phone": "+1 555-111-2233"
}
```

---

## 🧠 Prompt Engineering Concepts

- Zero-shot Prompting
- Few-shot Prompting
- Delimiters
- Temperature = 0
- Structured JSON Extraction

---

## 📈 Future Improvements

- Batch processing
- PDF document extraction
- Resume parsing
- OCR integration
- Streamlit Web Interface

---

## 👩‍💻 Author

**Eisha Naeem**

Computer Engineering Student
