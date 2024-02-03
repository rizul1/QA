# QA
# 48 Laws of Power Q&A Web App

This is a simple web application built with Streamlit that allows users to ask questions related to "The 48 Laws of Power." The app extracts information from the provided document and provides answers using OpenAI's language model.

## Features

- Ask questions about "The 48 Laws of Power" without explicitly mentioning the book or its title in the question.
- Information extraction from the document using PyPDFLoader and OpenAI embeddings.
- Similarity search and question-answering capabilities.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/rizul1/QA.git

2. Install the required dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run QA.py

4. Open your web browser and go to 'http://localhost:8501'.

5. Enter a question in the input field and click the "Get Answer" button.

## Note
The app only provides information based on the content of the provided document about "The 48 Laws of Power."
Users do not need to explicitly mention the book or its title in the question.




