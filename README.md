# LinkedIn Post Generator using Generative AI 🧠✍️

This project generates professional LinkedIn posts based on **topic**, **length**, and **language** (English or Hinglish), using **Large Language Models (LLMs)**.

## 🚀 Features

- Generate posts by selecting:
  - **Topic** (Tag)
  - **Length** (Short / Medium / Long)
  - **Language** (English / Hinglish)
- Automatically extracts and processes metadata
- Streamlined UI with **Streamlit**
- Supports tag unification for smarter post categorization

## 🛠️ Tech Stack

- 🐍 Python
- 🧠 LangChain + Groq API (LLM backend)
- 📄 JSON for post storage
- 🎨 Streamlit for user interface
- 🔄 Git & GitHub for version control

## 📂 Folder Structure
```bash
GenAI-project/
│
├── main.py                # Streamlit UI
├── llm_helper.py          # LLM chain helper logic
├── preprocess.py          # Metadata extraction using LLM
├── post_generator.py      # Post creation logic using tags, length, language
├── few_shot.py            # Few-shot examples for consistent generation
│
├── data/
│   ├── raw_posts.json         # Input data
│   └── processed_posts.json   # Output after preprocessing
│
├── tests/                           # All test files and documentation
│   ├── edge_case_tests.md           # Document for edge case test scenarios
│   ├── edge_case_tests.py           # Python script to test edge cases
│
│   ├── error_handling_tests.md      # Document for error-handling test results
│   ├── test_error_handling.py       # Script to test robustness and exceptions
│
│   ├── prompt_response_test.md      # Document detailing prompt quality and results
│   ├── promt_test.py                # Python script to validate prompt generation
│
│   ├── test_hinglish_generation.md  # Hinglish-specific testing documentation
│   ├── test_hinglish_generation.py  # Test script for Hinglish generation accuracy
│
│   └── ui_ux_tests.md               # UI/UX feedback & screenshot documentation
│
├── requirements.txt           # All the dependencies
├── .gitignore             # Files/folders to ignore in Git
└── README.md              # Project description and usage instructions

```
# 📦 Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app:
```bash
streamlit run main.py

