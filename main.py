import random
from itertools import chain
from typing import Tuple, List


def make_candidate(digits: str, fillers: List[str]) -> str:
    return "".join(chain.from_iterable(zip(digits, fillers))) + digits[-1]


def find_match(fillers: Tuple[str, str, str], digits: str, target: int) -> set:
    result = set()
    candidates = set()
    empty_spaces = len(digits) - 1
    possibilities = len(fillers) ** empty_spaces
    while len(candidates) < possibilities:
        fillers_combination = [random.choice(fillers) for _ in range(empty_spaces)]
        candidate = make_candidate(digits, fillers_combination)
        if eval(candidate) == target:
            result.add(candidate)
        candidates.add(make_candidate(digits, fillers_combination))
    return result


if __name__ == "__main__":
    print(
        *find_match(digits="9876543210", fillers=("+", "-", ""), target=200), sep="\n"
    )
