from dotenv import load_dotenv
from groq import Groq
from os import environ as env
from sys import argv

load_dotenv()

def main():
    if len(argv) > 1:
        user_prompt = argv[1]
    else:
        user_prompt = ""

    if not user_prompt: 
        print("Insert a prompt as an argument")
        return
        
    client = Groq(
        api_key=env.get("GROQ_API_KEY"),
    )

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        print(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
