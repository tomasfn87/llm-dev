from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
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
            model="gemini-2.5-flash-image",
            contents=[user_prompt])
        for part in response.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = part.as_image()
                image.save("generated_image.png")
                image.show()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()