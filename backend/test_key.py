import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env from current directory
load_dotenv()

KEY = os.getenv("GOOGLE_API_KEY")

print(f"Testing key: {KEY[:5] if KEY else 'None'}...{KEY[-5:] if KEY else 'None'}")

if not KEY:
    print("ERROR: No API Key found in environment variables.")
    exit(1)

try:
    genai.configure(api_key=KEY)
    print("Configuration set. Attempting to list models...")
    
    # Simple call to check auth
    models = [m.name for m in genai.list_models()]
    print(f"SUCCESS! Available models: {models[:3]}...")
    
    print("Attempting generation with 'gemini-pro'...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hello from Power Move diagnostic.")
    print(f"Generation Response: {response.text}")
    
except Exception as e:
    print("\n--- DIAGNOSTIC REPORT ---")
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")
    print("-------------------------")
