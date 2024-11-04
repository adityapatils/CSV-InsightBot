# 👨‍💻 Talk with Your Multi-CSV Data

Overview

**Talk with Your Multi-CSV Data** is a Streamlit web application designed to allow users to interact with multiple CSV files containing patient vital records and profile information. Leveraging advanced AI capabilities, users can ask questions about the data, and the application will provide meaningful insights based on the information in the CSV files.



## Project Features

- Upload and analyze multiple CSV files containing patient data.
- Use AI to answer queries related to the data, including patient profiles and vital signs.
- Interactive user interface for seamless data exploration.
- Leverages advanced models for natural language processing to interpret user queries.

## Requirements

This project requires the following Python packages, which can be installed via `requirements.txt`:

- `langchain`
- `langchain_community`
- `pandasai`
- `ollama`
- `streamlit`
- `groq`
- `langchain-groq`
- `python-dotenv`

## Setup Instructions

### 1. Create a Virtual Environment

To clone this repository to your local machine, use the following command
```bash 
git clone https://github.com/adityapatils/CSV-InsightBot.git
cd CSV-InsightBot

## Create a virtual environment, run the following commands:
python -m venv myvenv

# Activate the virtual environment
# On Windows
myvenv\Scripts\activate
# On macOS/Linux
source myvenv/bin/activate
```

### 2. Install Required Packages

After activating the virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

To enable API access for the application, you need to set up your GROQ API key. Create a file named `.env` in the root directory of your project and add the following line, replacing `your_api_key` with your actual key:

```
GROQ_API_KEY=''
```

You can obtain your GROQ API key from [GROQ Console](https://console.groq.com/keys).

### 4. Run the Application

To start the Streamlit application, run the following command:

```bash
streamlit run app.py
```

Open your browser and navigate to the URL provided in the terminal (usually `http://localhost:8501`) to access the application.

## Usage Instructions

1. **Upload CSV Files**: Use the sidebar to upload one or more CSV files containing patient vital records. 
2. **Select a File**: After uploading, select one of the uploaded CSV files from the dropdown menu.
3. **View Data**: The application will display the first 10 rows of the selected CSV file.
4. **Ask Questions**: In the query section, enter your question about the data. Here are some example queries you can ask:
   - "What is the max age of the patient from the record, and what is his/her name?"
   - "On which date was blood pressure highest and for which patient?"
   - "Provide us the list of patients based on blood pressure reading in descending order, highest blood pressure patient name will appear first then second highest and so on."
5. **Get Insights**: Click the "💬 Ask CSV" button to process your query. The application will display the results, either as structured text or as a table.

## Project Structure

```
Talk-with-Your-Multi-CSV-Data/
│
├── app.py               # Main application file
├── vital.csv            # Sample CSV file with patient vital records
├── requirements.txt     # List of required Python packages
└── .env                 # Environment variables file (GROQ API key)
```

## Acknowledgments

- **Streamlit**: For providing an easy way to build interactive web applications in Python.
- **Langchain and PandasAI**: For facilitating advanced natural language processing and data analysis.
- **GROQ**: For enabling efficient querying of data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

