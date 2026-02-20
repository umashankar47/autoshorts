"""
Simple LLM Chat Script
Uses Groq API for free LLM access
"""

from groq import Groq
import os

# Initialize Groq client
# Get your free API key from: https://console.groq.com/keys
client = Groq(api_key="")  # Replace with your actual key

def get_ai_response(user_input, model="llama-3.3-70b-versatile"):
    """
    Send input to AI and get detailed response

    Args:
        user_input (str): Your question or prompt
        model (str): Model to use (default: llama-3.1-70b-versatile)

    Returns:
        str: AI's response
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=model,
            temperature=0.7,  # Controls creativity (0-2, higher = more creative)
            max_tokens=2048,  # Maximum length of response
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def chat_session():
    """Interactive chat session with the AI"""
    print("=" * 60)
    print("AI Chat Session Started (type 'quit' to exit)")
    print("=" * 60)

    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        # Exit condition
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break

        # Skip empty inputs
        if not user_input:
            continue

        # Get AI response
        print("\nAI: Thinking...")
        response = get_ai_response(user_input)
        print(f"\nAI: {response}")


def single_query(question):
    """Single question/answer interaction"""
    print(f"\nQuestion: {question}")
    print("\nAI Response:")
    print("-" * 60)
    response = get_ai_response(question)
    print(response)
    print("-" * 60)
    return response


# Example usage
if __name__ == "__main__":
    # Choose one of these modes:

    # MODE 1: Interactive chat session
    chat_session()

    # MODE 2: Single query (comment out chat_session() above and uncomment below)
    # single_query("Explain quantum computing in simple terms")

    # MODE 3: Programmatic use (uncomment to use)
    # questions = [
    #     "What is Python?",
    #     "How do I create a list in Python?",
    #     "Explain list comprehensions with examples"
    # ]
    #
    # for q in questions:
    #     response = get_ai_response(q)
    #     print(f"\nQ: {q}")
    #     print(f"A: {response}\n")
