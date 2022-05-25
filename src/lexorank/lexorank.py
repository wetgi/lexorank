from typing import Optional, Tuple

MIN_CHAR = ord("0")
MAX_CHAR = ord("z")


def mid(prev: str, next: str) -> int:
    return (ord(prev) + ord(next)) // 2


def getChar(s: str, i: int, default_char: str) -> int:
    if i >= len(s):
        return ord(default_char)
    return ord(s[i])


# Rank returns a new rank string between prev and next.
# false if it needs to be reshuffled. e.g. same or adjacent prev, next values.
def lexorank(prev: str, next: Optional[str] = None) -> Tuple[str, bool]:
    if prev == "":
        prev = chr(MIN_CHAR)

    if next is None or next == "":
        next = chr(MAX_CHAR)

    rank = ""
    i = 0

    while True:
        prev_char = getChar(prev, i, chr(MIN_CHAR))
        next_char = getChar(next, i, chr(MAX_CHAR))

        if prev_char == next_char:
            rank += chr(prev_char)
            i = i + 1
            continue

        mid_char = mid(chr(prev_char), chr(next_char))
        if mid_char == prev_char or mid_char == next_char:
            rank += chr(prev_char)
            i = i + 1
            continue

        rank += chr(mid_char)
        break

    if rank >= next:
        return prev, False

    return rank, True
