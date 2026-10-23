# 🤖 AI Q&A Chatbot using LangChain & Groq

An AI-powered Question and Answer chatbot built using **Python, LangChain, Groq API, and Streamlit**. The application allows users to ask questions and receive AI-generated responses through an interactive chat interface. It also maintains conversation history during the active Streamlit session.

## 🚀 Features

- 💬 Interactive chat interface using Streamlit.
- 🧠 AI-generated responses using a Groq-hosted language model.
- 🔗 LangChain integration for invoking the language model.
- 📝 Conversation history using Streamlit session state.
- 🔐 Secure API key management using environment variables.
- ⚡ Fast response generation through Groq.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **LLM Integration:** LangChain
- **LLM Provider:** Groq
- **Model:** `openai/gpt-oss-120b`
- **Frontend:** Streamlit
- **Environment Management:** python-dotenv

## 📂 Project Structure

```text
00_qna_bot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd 00_qna_bot
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install langchain-groq streamlit python-dotenv
```

### 4. Configure the Groq API Key

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Important:** Never share your API key or upload your `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 💡 How It Works

1. **Environment Setup:** `python-dotenv` loads environment variables from the `.env` file.
2. **LLM Initialization:** `ChatGroq` initializes the Groq-hosted `openai/gpt-oss-120b` model.
3. **Chat Interface:** Streamlit displays the chatbot interface and accepts user questions.
4. **Conversation History:** `st.session_state` stores user messages and assistant responses during the active session.
5. **LLM Invocation:** `llm.invoke()` sends the conversation history to the language model.
6. **Response Display:** The chatbot displays the generated response in the chat interface.

## 📸 Application Preview

The application provides a simple chat interface where users can enter questions and receive AI-generated answers in real time.

## 🔮 Future Improvements

- Add a clear-chat button.
- Improve error handling for API failures.
- Add streaming responses.
- Support PDF and document-based question answering using RAG.
- Add persistent chat history.
- Improve conversation management and UI design.

## 👩‍💻 Author

**Pratiksha Bhagat**

AI Developer | Python | LangChain | Generative AI | LLM Applications

## 📄 License

This project is available for learning and educational purposes. Add a specific open-source license if you intend to distribute it under one.
