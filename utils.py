from difflib import SequenceMatcher


def format_output(title: str, content: str) -> str:
    separator = "=" * 50
    return f"\n{separator}\n{title}\n{separator}\n{content}\n"
