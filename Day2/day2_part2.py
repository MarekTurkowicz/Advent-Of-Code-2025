def is_invalid_part2(n: int) -> bool:
    """
    Returns True if the number consists of a digit sequence
    repeated at least two times.

    Valid examples:
        12341234      -> "1234" repeated 2 times
        123123123     -> "123" repeated 3 times
        1212121212    -> "12" repeated 5 times
        1111111       -> "1" repeated 7 times

    Rules:
    - The number cannot start with a leading zero.
    - Let 'chunk' be the prefix of the number. For each possible chunk length:
        * The total length of the number must be divisible by chunk length.
        * The number of repeats must be at least 2.
        * The number must exactly equal chunk repeated N times.

    If any valid repeating structure is found, the ID is considered invalid.
    """
    s = str(n)

    if s[0] == "0":
        return False

    length = len(s)

    for chunk_len in range(1, length // 2 + 1):
        if length % chunk_len != 0:
            continue

        repeats = length // chunk_len
        if repeats < 2:
            continue

        chunk = s[:chunk_len]

        if chunk * repeats == s:
            return True

    return False


def read_ranges(path: str):
    with open(path, encoding="utf-8") as f:
        line = f.read().strip()
    return [tuple(map(int, part.split("-"))) for part in line.split(",")]


def main_part2():
    ranges = read_ranges("Day2/input_day2.txt")

    total = 0
    count = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_invalid_part2(n):
                total += n
                count += 1

    print(f"Invalid IDs count: {count}")
    print(f"Sum of invalid IDs: {total}")


if __name__ == "__main__":
    main_part2()
