import os
from functools import lru_cache
from groq import Groq


# ---------------- CLIENT SINGLETON ----------------
@lru_cache()
def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError("❌ GROQ_API_KEY is missing")

    return Groq(api_key=api_key)


# ---------------- MAIN LLM CALL ----------------
def ask_llm(prompt: str) -> str:
    client = get_client()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content