#chatbot.py
import google.generativeai as genai
from . import config

class GeminiChatbot:
    def __init__(self):
        """Initialize the Gemini chatbot."""
        if not config.GOOGLE_API_KEY:
            raise ValueError("API key not found in environment variables")
            
        # Configure the Gemini API
        genai.configure(api_key=config.GOOGLE_API_KEY)
        
        # Initialize the model and chat
        self.model = genai.GenerativeModel(config.MODEL_NAME)
        self.chat = self.model.start_chat(history=[])
        
    def ask_question(self, question: str) -> str:
        """
        Send a question to the chatbot and get a response.
        
        Args:
            question (str): The user's question
            
        Returns:
            str: The chatbot's response
        """
        try:
            response = self.chat.send_message(question)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_chat_history(self) -> list:
        """Get the current chat history."""
        return self.chat.history
    
    def clear_chat_history(self) -> None:
        """Clear the chat history and start a new chat."""
        self.chat = self.model.start_chat(history=[])

def main():
    # Example usage of the chatbot
    try:
        print("Initializing Gemini Chatbot...")
        chatbot = GeminiChatbot()
        
        print("\nChatbot ready! Type 'quit' to exit or 'clear' to clear chat history.")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
                
            if user_input.lower() == 'clear':
                chatbot.clear_chat_history()
                print("Chat history cleared!")
                continue
            
            response = chatbot.ask_question(user_input)
            print(f"\nChatbot: {response}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()