import os
import sys
from dotenv import load_dotenv

load_dotenv()

# Add root directory to python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import sdk.key_manager as km
from llm import get_llm

def run_tests():
    print("==================================================")
    print("TEST 1: Rotating key on 'each_call' strategy")
    print("==================================================")
    km.ROTATION_STRATEGY = "each_call"
    km.current_index = 0
    km.key_usage = {i: 0 for i in range(len(km.API_KEYS))}

    llm_instance = get_llm()

    for i in range(3):
        print(f"\n--- Call {i+1} ---")
        print(f"Active Key Index BEFORE invocation: {km.current_index}")
        response = llm_instance.invoke("Hi, tell me a 1-word greeting")
        print(f"Response: {response.content.strip()}")
        print(f"Active Key Index AFTER invocation: {km.current_index}")

    print("\n==================================================")
    print("TEST 2: Rotating key on 'token_limit' strategy")
    print("==================================================")
    km.ROTATION_STRATEGY = "token_limit"
    km.TOKEN_LIMIT_PER_KEY = 50  # set a very low limit to trigger rotation
    km.current_index = 0
    km.key_usage = {i: 0 for i in range(len(km.API_KEYS))}

    print(f"Initial Key Index: {km.current_index}")
    
    # First call - should utilize some tokens (around 30-40) but not exceed 50 tokens
    print("\n--- Call 1 ---")
    response = llm_instance.invoke("Hi")
    print(f"Response: {response.content.strip()}")
    print(f"Key Index after Call 1 (limit={km.TOKEN_LIMIT_PER_KEY}): {km.current_index}")

    # Second call - will definitely push cumulative usage past 50 tokens and trigger rotation
    print("\n--- Call 2 ---")
    response = llm_instance.invoke("Describe Python in one sentence")
    print(f"Response: {response.content.strip()}")
    print(f"Key Index after Call 2 (limit={km.TOKEN_LIMIT_PER_KEY}): {km.current_index}")

    # Third call - using the new key
    print("\n--- Call 3 ---")
    response = llm_instance.invoke("Say ok")
    print(f"Response: {response.content.strip()}")
    print(f"Key Index after Call 3 (limit={km.TOKEN_LIMIT_PER_KEY}): {km.current_index}")

if __name__ == "__main__":
    run_tests()
