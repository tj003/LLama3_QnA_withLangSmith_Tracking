🔗 LangChain + Ollama + Streamlit AI Assistant
This project is a simple web-based chatbot built using LangChain, Ollama, and Streamlit, powered by the LLaMA3 model. It allows you to ask natural language questions and get responses from a local LLM.

🚀 Features
🤖 Ask questions to a local LLM via Ollama (llama3)

🔗 Uses LangChain's composable chains

🧪 Built-in LangSmith (open-source) tracing for debugging and observability

🌐 Streamlit-based interactive frontend

🔒 Secure API key management with .env

📦 Requirements
Python 3.8+

Ollama installed and running

Model llama3 pulled locally via Ollama

Optional: LangSmith account (free tier available)

🧰 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/langchain-ollama-app.git
cd langchain-ollama-app
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Pull the Ollama model:

bash
Copy
Edit
ollama pull llama3
Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=sk-xxx       # Optional, for fallback or LangSmith metadata
LANGCHAIN_API_KEY=ls-xxx    # Get from https://smith.langchain.com
LANGCHAIN_PROJECT=Ollama-Demo
▶️ Run the App
Make sure Ollama is running in the background:

bash
Copy
Edit
ollama serve
Then start the app:

bash
Copy
Edit
streamlit run app.py
🔍 LangSmith Tracing (Open-Source Observability)
This app supports LangSmith — an open-source tracing and observability tool built by the LangChain team.

Why use it?
📊 Visualize and debug chain calls

🪄 Inspect prompt templates and LLM outputs

⏱️ Measure latency and performance

How to enable it?
Set these in your environment:

env
Copy
Edit
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=Ollama-Demo
👉 Go to smith.langchain.com to view the traces (login required, free to use).

Note: This is optional, but highly recommended for development and debugging.

🧪 Example Usage
Type:

csharp
Copy
Edit
What is quantum computing?
Get:

css
Copy
Edit
Quantum computing is a type of computation that uses quantum bits to perform operations...
📁 File Structure
bash
Copy
Edit
langchain-ollama-app/
├── app.py              # Streamlit application
├── .env                # Environment variables
├── requirements.txt    # Required Python packages
└── README.md           # This documentation
📚 Tech Stack
LangChain

Ollama

LLaMA 3

Streamlit

LangSmith (Open Source Tracing)

