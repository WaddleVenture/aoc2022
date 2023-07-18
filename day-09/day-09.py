def touch(A, B, n):
    # Use Chebyshev distance
    xa, ya = A
    xb, yb = B
    chebyshev = max(abs(xa - xb), abs(ya - yb))
    return chebyshev == n


def solve_part1(data):
    # First part solution

    pairs = [elt.split(" ") for elt in data.split("\n")]
    # [['R', '4'], ['U', '4']]
    d, n = zip(*[(x, int(y)) for x, y in pairs])
    # ('R', 'U') (4, 4)

    x, y = 0, 0
    head = [(x, y)]
    tail = [(x, y)]

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for i in range(len(pairs)):
        for _ in range(n[i]):
            dx, dy = directions[d[i]]
            x += dx
            y += dy

            head.append((x, y))
            # Add the step to head

            if touch(head[-1], tail[-1], 1):
                # Check if the new head and last tail are touching
                tail.append(tail[-1])
                # If so just add the last tail because it don't have to move
            else:
                # Add the new tail coordinate
                tail.append(head[-2])

    return len(set(tail))


def solve_part2(data):
    # Second part solution
    pass


def test():
    # Test data
    test_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    # Solve Part 1 with test data
    part1_solution = solve_part1(test_input)
    print(f"Part 1 solution (test): {part1_solution}")

    # Solve Part 2 with test data
    part2_solution = solve_part2(test_input)
    print(f"Part 2 solution (test): {part2_solution}")


def main():
    # Read the input file
    with open("input.txt", "r") as file:
        data = file.read().strip()

    # Solve Part 1
    part1_solution = solve_part1(data)
    print(f"Part 1 solution: {part1_solution}")

    # Solve Part 2
    part2_solution = solve_part2(data)
    print(f"Part 2 solution: {part2_solution}")


if __name__ == "__main__":
    test()  # Run the test function
    # main()
