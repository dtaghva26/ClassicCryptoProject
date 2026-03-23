from typing import List, Tuple

def print_trace(title: str, history: List[Tuple[str, str]]):
    print(f"\n[{title}]")

    for step, value in history:
        print(f"{step}: {value}")