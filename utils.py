from difflib import SequenceMatcher

def format_output(title: str, content: str) -> str:
    separator = "=" * 50
    return f"\n{separator}\n{title}\n{separator}\n{content}\n"

def calculate_similarity(text1: str, text2: str) -> float:
    return SequenceMatcher(None, text1, text2).ratio()
