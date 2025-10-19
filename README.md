# 🧠 Assignment: RAG with Playwright and Pytest Framework

## 📄 Overview
This assignment demonstrates how to:
1. Create a **Retrieval-Augmented Generation (RAG)** pipeline that reads a **10-page document (PDF)**, chunks and indexes it, and answers questions based on the content.  
2. Use **Playwright MCP** to create and run test scripts.  
3. Build a **Pytest framework** around those scripts.  
4. Use **Chain-of-Thought (CoT)** and **Reflexive Prompting** to generate a **job headline** for a job search.

---

## 📁 Folder / File Description

| File / Folder | Description |
|----------------|-------------|
| `pdf_file1.py` | Reads and extracts text from PDF. |
| `rag_document.py` | Handles RAG logic: chunking, embedding, indexing, and answering queries. |
| `job_headline_generator.py` | Generates job headline using chain-of-thought and reflexive prompting. |
| `pages/` | Contains Playwright page object files (`login_page.py`, `dashboard_page.py`). |
| `tests/` | Contains Playwright MCP test scripts. |
| `conftest.py` | Pytest configuration and shared fixtures for Playwright tests. |
| `test_login.py` | Example Playwright test case. |
| `pytest.ini` | Pytest settings. |
| `sample.pdf` | Example 10-page document used for RAG. |

---

## ⚙️ How to Run

### 1️⃣ Install Dependencies
```bash
2️⃣Run the RAG Script
python rag_document.py --input sample.pdf
3️⃣ Ask a Question
python rag_document.py --query "Summarize the document in 3 lines."
4️⃣ Generate Job Headline
python job_headline_generator.py

5️⃣ Run Playwright Tests
pytest tests/

🔑 Environment Variables

Create a .env file with:

OPENAI_API_KEY=your_api_key

🧪 Summary of Assignment Tasks

✅ Created RAG pipeline with a 10-page document
✅ Implemented chunking, embedding, and indexing
✅ Performed Q&A on indexed data
✅ Created Playwright test scripts using MCP
✅ Built Pytest-based framework
✅ Used chain-of-thought and reflexive prompting for headline generation

📌 Notes

All code is written in Python.

LangChain and FAISS are used for RAG pipeline.

Playwright is used for browser automation.

Pytest is used for test framework execution.


---

✅ **Just copy all of the text above** (from the first `# 🧠 Assignment:` line to the last line)  
and paste it directly into your `README.md` file.  

That’s the final, clean version suitable for your **assignment submission** — short, clear, and complete.

pip install -r requirements.txt
playwright install
