import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("\n=== Available Models ===")
for model in genai.list_models():
    print(f"\nModel: {model.name}")
    print(f"  Supported methods: {model.supported_generation_methods}")
    print(f"  Display name: {model.display_name}")
