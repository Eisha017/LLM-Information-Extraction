# Prompt Engineering Report

## Objective

The objective of this project is to transform unstructured textual information into structured JSON using a Large Language Model.

---

## Why Zero-shot Prompting?

Zero-shot prompting provides only instructions to the LLM without any examples.

This evaluates the model's ability to understand the task using natural language instructions alone.

Advantages

- Simple
- Quick
- Minimal prompt size

Limitations

- Less consistent on difficult inputs
- May misunderstand unusual formatting

---

## Why Few-shot Prompting?

Few-shot prompting includes example input-output pairs before the actual task.

The examples teach the model the desired format and improve consistency.

Advantages

- Better accuracy
- More reliable JSON
- Handles messy text better

Limitations

- Longer prompts
- Higher token usage

---

## Why Delimiters?

The input text is enclosed using

###
User Input
###

This clearly separates:

- Instructions
- Examples
- Actual data

Without delimiters, the model may confuse the input text with the instructions.

Using delimiters significantly improves prompt clarity and reduces ambiguity.

---

## Why Temperature = 0?

Temperature controls randomness.

Temperature = 0 makes the model deterministic.

Benefits

- Consistent outputs
- Stable JSON formatting
- Repeatable extraction

This is particularly important for information extraction systems where reliability is preferred over creativity.

---

## Conclusion

Prompt engineering techniques such as Few-shot Prompting, Delimiters, and Temperature Control significantly improve the consistency and reliability of structured information extraction from unstructured text.
