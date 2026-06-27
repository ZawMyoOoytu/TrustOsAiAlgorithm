import json
import re
import logging
from typing import Any


# =========================
# REMOVE MARKDOWN
# =========================
def clean_llm_output(raw: str) -> str:
    """
    Remove markdown wrappers from LLM response
    """

    if not raw:
        return ""

    text = str(raw)

    # Remove code fences
    text = text.replace("```json", "")
    text = text.replace("```JSON", "")
    text = text.replace("```", "")

    return text.strip()



# =========================
# SANITIZE OBJECT
# =========================
def sanitize_json_object(obj: Any):
    """
    Normalize parsed JSON object
    """

    if isinstance(obj, dict):
        return {
            key: sanitize_json_object(value)
            for key, value in obj.items()
        }

    if isinstance(obj, list):
        return [
            sanitize_json_object(item)
            for item in obj
        ]

    if isinstance(obj, str):

        # Remove dangerous characters
        return (
            obj
            .replace("\r", "")
            .strip()
        )

    return obj



# =========================
# EXTRACT JSON BLOCK
# =========================
def extract_json_block(text: str):

    """
    Extract JSON object from mixed output
    """

    try:

        matches = re.findall(
            r"\{[\s\S]*\}",
            text
        )

        if not matches:
            return None


        # biggest JSON candidate
        candidates = sorted(
            matches,
            key=len,
            reverse=True
        )


        for candidate in candidates:

            try:
                return json.loads(candidate)

            except Exception:
                continue


    except Exception as e:

        logging.warning(
            f"JSON extraction failed: {e}"
        )


    return None



# =========================
# MAIN SAFE PARSER
# =========================
def safe_parse_llm_output(raw: Any):
    """
    TrustOsAi Universal LLM Output Parser

    Flow:

    Raw LLM
        |
        v
    Clean markdown
        |
        v
    JSON parse
        |
        v
    Extract JSON
        |
        v
    Sanitize
        |
        v
    Safe response
    """

    # Already JSON object
    if isinstance(raw, dict):

        return sanitize_json_object(raw)



    cleaned = clean_llm_output(raw)



    # =====================
    # STEP 1
    # DIRECT JSON PARSE
    # =====================
    try:

        result = json.loads(cleaned)

        return sanitize_json_object(result)


    except Exception:

        logging.warning(
            "Direct JSON parsing failed"
        )



    # =====================
    # STEP 2
    # JSON EXTRACTION
    # =====================
    extracted = extract_json_block(
        cleaned
    )


    if extracted:

        return sanitize_json_object(
            extracted
        )



    # =====================
    # STEP 3
    # FALLBACK
    # =====================
    logging.error(
        "LLM returned invalid JSON"
    )


    return {

        "type": "error",

        "title": "Parse Error",

        "description":
            "Model did not return valid JSON format",

        "raw":
            str(raw)[:1000],

        "language":
            "text",

        "files":
            [],

        "steps":
            []

    }