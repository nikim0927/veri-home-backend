def calculate_risk(confidence: float, is_structural: bool) -> float:
    """
    Calculate risk rating based on structural change and AI confidence.

    Logic:
    - If is_structural is True, return 1.0 (maximum risk).
    - If False, return (1.0 - confidence).

    :param confidence: The confidence score (0.0 to 1.0).
    :param is_structural: A boolean indicating if the issue is structural.
    :return: A float representing the risk score.
    """
    if is_structural:
        return 1.0
    return 1.0 - confidence
