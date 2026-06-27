def get_output_contract(intent: str) -> dict:

    contracts = {
        "design_request": {
            "mode": "structured_design",
            "strict": True,
            "no_explanation": True
        },

        "website_generation": {
            "mode": "code_generation",
            "strict": True,
            "no_explanation": True
        },

        "knowledge_query": {
            "mode": "normal",
            "strict": True,
            "no_explanation": True
        },

        "general_task": {
            "mode": "normal",
            "strict": True,
            "no_explanation": True
        },

        "risky_task": {
            "mode": "blocked",
            "strict": True,
            "no_execution": True
        }
    }

    return contracts.get(intent, contracts["general_task"])