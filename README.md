🧠 Chatbot using OpenAI GPT
This is a simple command-line chatbot built with Python and the OpenAI GPT API (gpt-3.5-turbo). The chatbot interacts with users in natural language, answers questions, and maintains a friendly conversation.

✨ Features
Integrates with OpenAI's Chat API

Interactive CLI (Command Line Interface)

Continuously responds until user exits

Easy to customize for other use-cases

🛠️ Technologies Used
Python

OpenAI Python SDK

.env file for storing API keys (optional, but recommended)

🚀 Getting Started
1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/chatbot.git
cd chatbot
2. Install dependencies:
bash
Copy
Edit
pip install openai python-dotenv
3. Set your OpenAI API key:
Option 1 (recommended):
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Option 2 (temporary):
Set it directly in your script (not recommended for security):

python
Copy
Edit
openai.api_key = "your-api-key"
4. Run the chatbot:
bash
Copy
Edit
python chatbot.py
📌 Example
vbnet
Copy
Edit
You: What is Python?
Chatbot: Python is a high-level, interpreted programming language known for its readability and versatility...
🔒 Note
Always keep your API key secure. Use environment variables or .env files and add .env to your .gitignore.
