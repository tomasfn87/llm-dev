from dotenv import load_dotenv
from openai import OpenAI
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
        
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=env.get("OPENAI_API_KEY"),
    )

    try:
        response = client.responses.create(
            model="openai/gpt-oss-20b:free",
            input=user_prompt
        )
        print(response.output_text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()