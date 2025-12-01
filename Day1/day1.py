def count_zero_positions(instructions):
    """
    Day 1: Part1 - Dial Rotation Simulation
    Simulates dial rotations and counts how many times the dial lands on 0.
    Dial:
      - starts at 50
      - values wrap in range 0..99
    """
    position = 50
    zero_count = 0

    for line in instructions:
        line = line.strip()
        if not line:
            continue

        direction = line[0]  # 'L' or 'R'
        distance = int(line[1:])

        if direction == "L":
            position = (position - distance) % 100
        elif direction == "R":
            position = (position + distance) % 100
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if position == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    with open("day1/input.txt", encoding="utf-8") as f:
        data = f.readlines()

    result = count_zero_positions(data)
    print("Password:", result)
