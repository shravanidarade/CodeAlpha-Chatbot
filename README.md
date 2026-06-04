# CodeAlpha_Chatbot

A lightweight, interactive, rule-based chatbot built in Python. This project fulfills **Task 4 (Basic Chatbot)** for the CodeAlpha internship program, demonstrating foundational programming principles like user-defined functions, conditional tracking logic (`if-elif-else`), and iterative control flow loops.

## 🚀 Project Overview
The **CodeAlpha Chatbot** acts as an automated conversational assistant. It listens to user inputs via the terminal console, cleans and normalizes the text to handle irregular casing or spacing, matches the inputs against predefined rule criteria, and generates smart dynamic responses.

### 🛠️ Key Concepts Practiced
*   **Functions:** Modularized core logic separating the response parser (`get_bot_response`) from the console input runner (`run_chat_session`).
*   **Conditional Structures (`if-elif-else`):** Efficient branching structure optimized to parse phrases, keywords, and handle fallback conditions smoothly.
*   **Continuous Control Loops (`while`):** An persistent loop ensuring a seamless, life-like conversational flow until an exit command is issued.
*   **Input/Output Operations:** Standard library dynamic terminal interactions capturing string data.

---

## 📋 Features
*   **Input Normalization:** Automatically trims trailing white spaces and converts strings to lowercase, making variations like `"HELLO"`, `"Hello "`, and `"hello"` work identically.
*   **Multi-phrase Recognition:** Recognizes a broad scope of expressions for greetings, situational check-ins, capabilities exploration, and exit phrases.
*   **Interactive Menu Interface:** Displays clean text boundaries, clear directions, and custom emoji styling features.
*   **Graceful Fallbacks:** Uses an intuitive default responder to catch unknown sentences instead of encountering run-time errors or crashing.

---

## 💻 How to Run Locally

### Prerequisites
Make sure you have **Python 3.x** installed on your operating system. You can verify this by opening your command line interface and typing:
```bash
python --version
```

### Steps to Execute
1. Download or clone this repository to your local system workspace.
2. Open your terminal or command prompt tool (e.g., Command Prompt, PowerShell, Git Bash).
3. Change directories to the workspace folder where `CodeAlpha_Chatbot.py` is saved.
4. Launch the application script with the following command:
```bash
python CodeAlpha_Chatbot.py
```

---

## 💬 Sample Conversation Flow
```text
==================================================
🤖 Welcome to PythonBot, your friendly assistant! 🤖
Directions: Type your message below and press Enter.
Type 'bye' or 'exit' whenever you want to close the chat.
==================================================

You: Hello
Bot: Hi there! Friendly virtual greetings to you! 👋

You: how are you doing
Bot: I'm just a simple script, but I'm functioning perfectly! Thanks for asking! 💻

You: what can you do?
Bot: I can answer basic greetings! Try saying 'hello', 'how are you', or 'bye'.

You: Bye
Bot: Goodbye! Have a fantastic day ahead! 🚀

[Chat Session Closed]
```
