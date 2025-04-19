from dotenv import load_dotenv
import os

if __name__ == "__main__":
    print("hello langchain")
    load_dotenv()
    print(os.environ['SME_API_KEY'])
