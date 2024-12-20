# Gemini Chatbot

A simple question-answering chatbot using Google's Gemini API.
![image](https://github.com/user-attachments/assets/5d16d138-d170-4a65-bedc-7a239188f391)

## Setup

1. Clone the repository:
```bash
git clone <https://github.com/rajput-tarun/chatbot_genralpurpose.git>
cd gemini-chatbot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Google API key:
```env
GOOGLE_API_KEY=your_api_key_here
```

## Running the Chatbot

To start the chatbot, run:
```bash
python -m src.chatbot
```

## Commands
- Type 'quit' to exit the chatbot
- Type 'clear' to clear chat history

## Features
- Interactive chat interface
- Chat history management
- Environment variable configuration
- Error handling
  

