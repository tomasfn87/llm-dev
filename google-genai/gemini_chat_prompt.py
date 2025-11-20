from dotenv import load_dotenv
from google import genai
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
        
    client = genai.Client()

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=user_prompt
        )
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()