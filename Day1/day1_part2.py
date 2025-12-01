def count_zero_clicks(instructions):
    """
    Day 1: Part2 - Dial Rotation Simulation (method 0x434C49434B)
    Count how many times the dial points at 0 during ALL clicks.
    Dial:
      - starts at 50
      - values are 0..99, wrap modulo 100
    """
    position = 50
    zero_count = 0

    for line in instructions:
        line = line.strip()
        if not line:
            continue

        direction = line[0]  # 'L' or 'R'
        distance = int(line[1:])  # number of clicks
        step = -1 if direction == "L" else 1

        for _ in range(distance):
            position = (position + step) % 100
            if position == 0:
                zero_count += 1

    return zero_count


if __name__ == "__main__":
    with open("Day1/input2.txt", encoding="utf-8") as f:
        data = f.readlines()

    result = count_zero_clicks(data)
    print("Password (method 0x434C49434B):", result)
