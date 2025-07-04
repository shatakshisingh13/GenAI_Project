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
GenAI project/
│
├── main.py # Streamlit UI
├── preprocess.py # Metadata extraction
├── post_generator.py # Post creation logic
├── few_shot.py # Few-shot prompt examples
├── data/
│ ├── raw_posts.json
│ └── processed_posts.json
├── .gitignore
└── README.md

# 📦 Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the app:
```bash
streamlit run main.py

