# LLM Information Extraction using Prompt Engineering

A Python application that extracts structured information from unstructured text using Google's Gemini Large Language Model (LLM).

This project demonstrates practical Prompt Engineering techniques including Zero-shot Prompting, Few-shot Prompting, Delimiters, and Deterministic Generation (Temperature = 0).

---

## Features

- Extracts structured data from messy text
- Zero-shot prompting
- Few-shot prompting
- Prompt comparison
- JSON output
- Supports multiple input files
- Uses Gemini API
- Saves extracted information automatically

---

## Technologies

- Python
- Google Gemini API
- Prompt Engineering
- python-dotenv

---

## Information Extracted

- Name
- Company
- Job Title
- Email Address
- Phone Number

---

## Project Structure

```text
LLM-Information-Extraction/
│
├── app.py
├── prompt.py
├── fewshot_prompt.py
├── samples/
├── outputs/
└── docs/
```

---

## How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
python app.py
```

Enter the file name when prompted.

Example

```
samples/sample1.txt
```

---

## Example Input

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

## Example Output

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

## Prompt Engineering Concepts

- Zero-shot Prompting
- Few-shot Prompting
- Delimiters
- Temperature = 0
- Structured JSON Extraction

---

## Future Improvements

- Batch processing
- CSV export
- PDF document extraction
- Resume parsing
- OCR integration
- Web interface using Streamlit

---

## Author

Eisha Naeem

Computer Engineering Student