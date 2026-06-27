def detect_conflicts(policy: dict):

    conflicts = []

    if (
        policy.get("allow_reasoning") is True
        and
        policy.get("block_reasoning") is True
    ):
        conflicts.append(
            "allow_reasoning conflicts with block_reasoning"
        )

    return conflicts