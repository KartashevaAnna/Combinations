import random
from itertools import chain
from typing import Tuple, List


def make_candidate(digits: str, fillers: List[str]) -> str:
    return "".join(chain.from_iterable(zip(digits, fillers))) + digits[-1]


def find_match(fillers: Tuple[str, str, str], digits: str, target: int) -> chain | str:
    candidates = set()
    empty_spaces = len(digits) - 1
    possibilities = len(fillers) ** empty_spaces
    while len(candidates) < possibilities:
        fillers_combination = [random.choice(fillers) for _ in range(empty_spaces)]
        candidate = make_candidate(digits, fillers_combination)
        if eval(candidate) == target:
            return candidate
        candidates.add(make_candidate(digits, fillers_combination))
    return "Match not found"


if __name__ == "__main__":
    print(
        f"Result: {find_match(digits='9876543210', fillers=('+', '-', ''), target=200)}"
    )
