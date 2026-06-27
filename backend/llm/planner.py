from groq import Groq, BadRequestError
import os

from backend.core.llm_parser import safe_parse_llm_output


# =========================
# GROQ CLIENT
# =========================
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# =========================
# MODELS
# =========================
PRIMARY_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"


# =========================
# STRICT SYSTEM PROMPT (FIXED)
# =========================
SYSTEM_PROMPT = """
You are TrustOsAi Structured Execution Engine.

YOU MUST FOLLOW THESE RULES STRICTLY:

1. Output ONLY valid JSON
2. NO markdown (no ``` )
3. NO explanation text
4. NO extra keys outside schema
5. ALL strings must be properly escaped
6. DO NOT include raw multiline HTML inside a single string

IMPORTANT STRUCTURE RULE:

For websites:
- split into files array instead of single "code" string

REQUIRED OUTPUT FORMAT:

{
  "type": "text | code | website | api | app",
  "title": "string",
  "description": "string",

  "files": [
    {
      "name": "index.html",
      "content": "escaped string only"
    }
  ],

  "steps": [
    "step 1",
    "step 2"
  ],

  "language": "string"
}

BEHAVIOR RULES:
- website → use files[]
- code → single file in files[]
- text → no code needed
"""


# =========================
# INTERNAL CALL FUNCTION
# =========================
def _call_model(model: str, prompt: str):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content


# =========================
# MAIN FUNCTION
# =========================
def llm_plan(prompt: str):

    try:
        # =====================
        # 1. PRIMARY MODEL
        # =====================
        raw = _call_model(PRIMARY_MODEL, prompt)

    except BadRequestError:
        # =====================
        # 2. FALLBACK MODEL
        # =====================
        raw = _call_model(FALLBACK_MODEL, prompt)

    # =====================
    # 3. SAFE PARSE (IMPORTANT)
    # =====================
    parsed = safe_parse_llm_output(raw)

    # =====================
    # 4. FINAL SAFETY NORMALIZATION
    # =====================
    if not isinstance(parsed, dict):
        return {
            "type": "error",
            "title": "Parse Failure",
            "description": "Model output could not be parsed",
            "raw": raw[:1000]
        }

    return parsed