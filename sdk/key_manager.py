import os
from dotenv import load_dotenv

# Load environment variables from home directory (~/.groq_keys)
home_keys = os.path.expanduser("~/.groq_keys")
if os.path.exists(home_keys):
    load_dotenv(home_keys)
else:
    load_dotenv()

API_KEYS = []
ROTATION_STRATEGY = "each_call"
TOKEN_LIMIT_PER_KEY = 5000

# Try loading from streamlit secrets
try:
    import streamlit as st
    if hasattr(st, "secrets") and st.secrets:
        # Check if secrets exist at top-level
        API_KEYS = [
            st.secrets.get("GROQ_API_KEY_1"),
            st.secrets.get("GROQ_API_KEY_2"),
            st.secrets.get("GROQ_API_KEY_3"),
        ]
        API_KEYS = [k for k in API_KEYS if k]
        
        # If not at top-level, try nested under a 'groq' dict/namespace
        if not API_KEYS and "groq" in st.secrets:
            groq_secrets = st.secrets["groq"]
            API_KEYS = [
                groq_secrets.get("GROQ_API_KEY_1"),
                groq_secrets.get("GROQ_API_KEY_2"),
                groq_secrets.get("GROQ_API_KEY_3"),
            ]
            API_KEYS = [k for k in API_KEYS if k]

        if "ROTATION_STRATEGY" in st.secrets:
            ROTATION_STRATEGY = st.secrets["ROTATION_STRATEGY"]
        if "TOKEN_LIMIT_PER_KEY" in st.secrets:
            TOKEN_LIMIT_PER_KEY = int(st.secrets["TOKEN_LIMIT_PER_KEY"])
except Exception:
    pass

# Fallback to env variables if not found or empty
if not API_KEYS:
    API_KEYS = [
        os.getenv("GROQ_API_KEY_1"),
        os.getenv("GROQ_API_KEY_2"),
        os.getenv("GROQ_API_KEY_3"),
    ]
    API_KEYS = [key for key in API_KEYS if key]

if os.getenv("ROTATION_STRATEGY"):
    ROTATION_STRATEGY = os.getenv("ROTATION_STRATEGY")
if os.getenv("TOKEN_LIMIT_PER_KEY"):
    TOKEN_LIMIT_PER_KEY = int(os.getenv("TOKEN_LIMIT_PER_KEY"))

# State tracking
current_index = 0
key_usage = {i: 0 for i in range(len(API_KEYS))}



def get_current_key():
    global current_index

    if not API_KEYS:
        raise Exception(
            "No GROQ API Keys found in .env"
        )

    return API_KEYS[current_index]


def report_usage(tokens):
    global current_index

    if not API_KEYS:
        return

    key_usage[current_index] += tokens
    limit_str = f"/{TOKEN_LIMIT_PER_KEY}" if ROTATION_STRATEGY == "token_limit" else ""
    print(f"\n[Key Manager] Key Index {current_index} used {tokens} tokens. Total: {key_usage[current_index]}{limit_str}")

    should_rotate = False
    reason = ""

    if ROTATION_STRATEGY == "each_call" and tokens > 0:
        should_rotate = True
        reason = "rotation after token utilization"
    elif ROTATION_STRATEGY == "token_limit" and key_usage[current_index] >= TOKEN_LIMIT_PER_KEY:
        should_rotate = True
        reason = f"token limit of {TOKEN_LIMIT_PER_KEY} exceeded"

    if should_rotate:
        old_index = current_index
        current_index = (current_index + 1) % len(API_KEYS)
        print("==============================")
        print(f"[Key Manager] Rotating API Key: Index {old_index} -> Index {current_index} ({reason})")
        print("==============================\n")


def get_next_key():
    # Keep for backward compatibility with existing code calling get_next_key
    return get_current_key()