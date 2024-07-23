import streamlit as st
from langchain_helper import get_few_shot_db_chain

# Set the title of the Streamlit app
st.title("AtliQ T Shirts: Database Q&A 👕")

# Create an input box for the user to enter their question
question = st.text_input("Question: ")

# If the user has entered a question, proceed to handle it
if question:
    # Get the configured few-shot learning SQLDatabaseChain
    chain = get_few_shot_db_chain()
    
    # Run the chain with the user's question to get the response
    response = chain.run(question)

    # Display the answer
    st.header("Answer")
    st.write(response)
