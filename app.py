import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to initialize and interact with CSV data using an enhanced query approach
def chat_with_csv(df, query):
    # Load environment variables
    load_dotenv()
    
    # Initialize GROQ chat with API key and improved settings
    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name="llama3-70b-8192", 
        temperature=0.2
    )
    
    # Initialize SmartDataframe with DataFrame and LLM configuration
    pandas_ai = SmartDataframe(df, config={"llm": llm})

    # Build prompt for Chain of Thought reasoning and domain-specific insights
    prompt_template = (
        f"You are a data expert analyzing a medical dataset. "
        f"Answer the user's question with specific, detailed insights directly addressing the query. "
        f"Use the dataset to calculate and provide exact answers. "
        f"If the question is complex, break down your response into clear steps and reference "
        f"relevant columns in the data where appropriate."
    )
    
    # Chat with the DataFrame using the formatted query
    result = pandas_ai.chat(f"{prompt_template}\nQuery: {query}")
    return result

# Streamlit app configuration
st.set_page_config(layout='wide', page_title="Multi-CSV Data Chat", page_icon="🗂️")
st.title("👨‍💻 Talk with Your Multi-CSV Data")

# Sidebar for CSV file upload
with st.sidebar:
    st.header("📂 CSV File Upload")
    input_csvs = st.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)
    st.markdown(
        "Upload multiple CSV files to start analyzing your data. Select one file at a time for detailed insights."
    )

# Main section for CSV data analysis
if input_csvs:
    # Select a CSV file from the uploaded files using a dropdown menu
    selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
    selected_index = [file.name for file in input_csvs].index(selected_file)
    
    # Load and display the selected CSV file
    st.success(f"**CSV '{selected_file}' uploaded successfully**")
    data = pd.read_csv(input_csvs[selected_index])
    
    with st.expander("📊 View CSV Data"):
        st.dataframe(data.head(10), use_container_width=True)
    
    # Query section
    st.subheader("🔍 Chat with Your CSV Data")
    st.markdown("Enter your question below for detailed analysis and insights from the dataset.")
    input_text = st.text_area("Enter your question", placeholder="e.g., On which date was blood pressure highest and for which patient?")

    # Perform analysis on the query when button is clicked
    if input_text:
        if st.button("💬 Ask CSV"):
            st.info(f"**Your Question:** {input_text}")
            with st.spinner("Processing your question..."):
                result = chat_with_csv(data, input_text)
                
                # Display the result with improved formatting
                st.subheader("📋 Answer")
                if isinstance(result, pd.DataFrame):
                    st.write("The answer is provided as a table below:")
                    st.table(result)
                elif isinstance(result, str) and '\n' in result:
                    st.write("Here's the result in a well-structured format:")
                    st.markdown(f"```{result}```")
                else:
                    st.success(result)

else:
    st.warning("Please upload at least one CSV file to begin.")
