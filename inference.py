import os
from openai import OpenAI

def run_inference():
    # Scaler provides these automatically in the environment
    client = OpenAI(
        base_url=os.getenv("API_BASE_URL", "http://localhost:7860"),
        api_key=os.getenv("HF_TOKEN", "dummy_token")
    )
    
    print("Testing Easy Task...")
    # This simulates an LLM agent 'playing' your environment
    print("Task: SELECT * FROM users")
    print("Score: 1.0 (Simulated)")

if __name__ == "__main__":
    run_inference()