import streamlit as st
from langchain.document_loaders import PyPDFLoader,OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

# Load PDF using PyPDFLoader
loader = OnlinePDFLoader("https://pgcag.files.wordpress.com/2010/01/48lawsofpower.pdf")
data = loader.load()

# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_documents(data)

# Load embeddings into Chroma
embeddings = OpenAIEmbeddings(openai_api_key='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')
vectorstore = Chroma.from_documents(texts, embeddings)

# Create Streamlit app
st.title("48 Laws of Power Q&A")
st.write("This app only has information about 'The 48 Laws of Power'. You don't need to mention the book or '48 Laws of Power' in your question.")

# User input for the question
question = st.text_input("Ask a question about 'The 48 Laws of Power'")

# Perform similarity search and question-answering if a question is provided
if question:
    if st.button("Get Answer"):
        # Similarity search
        docs = vectorstore.similarity_search(question)

        # Question-answering
        llm = ChatOpenAI(temperature=0, openai_api_key='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')
        chain = load_qa_chain(llm, chain_type="stuff")
        answer = chain.run(input_documents=docs, question=question)

        # Display the answer
        st.write("Answer:", answer)
else:
    st.info("Please enter a question to get an answer.")
