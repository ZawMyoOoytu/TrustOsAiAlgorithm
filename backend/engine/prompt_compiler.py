class PromptCompiler:

    def compile(self, task: str, contract: dict, mode: str):

        # =========================
        # NORMAL MODE
        # =========================
        if not mode or not mode.startswith("structured"):

            return f"""
You are a helpful assistant.

Task:
{task}

Respond normally.
"""

        # =========================
        # STRUCTURED MODE (ZERO LANGUAGE GENERATION)
        # =========================

        contract = contract if isinstance(contract, dict) else {}

        schema = contract.get("schema", {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "data": {"type": "object"}
            },
            "required": ["type", "data"],
            "additionalProperties": False
        })

        return f"""
SYSTEM MODE: EXECUTION ENGINE ONLY

YOU ARE NOT AN ASSISTANT.
YOU ARE NOT A TEACHER.
YOU ARE NOT A WRITER.
YOU ARE NOT A LANGUAGE GENERATOR.

YOU ARE A PURE STRUCTURED OUTPUT MACHINE.

=================================================
HARD DISABLE FLAGS
=================================================
- DISABLE explanations
- DISABLE narrative text generation
- DISABLE tutorials
- DISABLE step-by-step reasoning
- DISABLE introductions
- DISABLE conclusions
- DISABLE paragraphs

=================================================
ONLY ALLOWED OUTPUT TYPE
=================================================
JSON OBJECT ONLY

=================================================
SCHEMA
=================================================
{schema}

=================================================
TASK
=================================================
{task}

=================================================
FINAL RULE
=================================================
RETURN ONLY RAW JSON. NO TEXT. NO WORDS. NO SENTENCES.
"""