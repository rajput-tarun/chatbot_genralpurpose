#app.py

from flask import Flask, render_template, request, jsonify
from .. import config
from ..chatbot import GeminiChatbot

app = Flask(__name__)
chatbot = None

def init_app():
    global chatbot
    chatbot = GeminiChatbot()
    return app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    
    response = chatbot.ask_question(question)
    return jsonify({'response': response})

def run_app():
    app = init_app()
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    run_app()