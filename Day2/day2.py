def is_invalid_part1(n: int) -> bool:
    """
    Returns True if the number consists of a digit sequence
    repeated exactly two times.

    Valid examples:
        11      -> "1" repeated twice
        6464    -> "64" repeated twice
        123123  -> "123" repeated twice

    Rules:
    - The number must have an even number of digits.
    - No leading zeros are allowed (012012 is not a valid ID).
    - The first half of the digits must be identical to the second half.

    If all conditions are met, the ID is considered invalid.
    """
    s = str(n)

    if len(s) % 2 != 0:
        return False

    if s[0] == "0":
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


def read_ranges(path: str):
    with open(path, encoding="utf-8") as f:
        line = f.read().strip()
    return [tuple(map(int, part.split("-"))) for part in line.split(",")]


def main_part1():
    ranges = read_ranges("Day2/input_day2.txt")

    total = 0
    count = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_part1(n):
                total += n
                count += 1

    print(f" Invalid IDs count: {count}")
    print(f"Sum of invalid IDs: {total}")


if __name__ == "__main__":
    main_part1()
