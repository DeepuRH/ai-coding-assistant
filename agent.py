import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

SYSTEM_PROMPT = """
You are an elite AI coding assistant.

Responsibilities:
- Explain Python code clearly
- Fix bugs step-by-step
- Optimize code
- Review uploaded files
- Suggest best practices
- Teach beginners simply
"""

chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def coding_agent(user_input, file_content=""):

    full_prompt = f"""
User Question:
{user_input}

Uploaded Code:
{file_content}
"""

    chat_history.append({
        "role": "user",
        "content": full_prompt
    })

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "baidu/cobuddy:free",
            "messages": chat_history
        }
    )

    result = response.json()

    reply = result["choices"][0]["message"]["content"]

    chat_history.append({
        "role": "assistant",
        "content": reply
    })

    return reply