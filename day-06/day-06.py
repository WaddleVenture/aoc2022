def solve_part1(data):
    # First part solution
    for i in range(len(data) - 3):
        marker = data[i:i+4]
        if len(set(marker)) == 4:
            return i+4

def solve_part2(data):
    # Second part solution
    for i in range(len(data) - 13):
        marker = data[i:i+14]
        if len(set(marker)) == 14:
            return i+14

def test():
    # Test data
    test_input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    
    # Solve Part 1 with test data
    part1_solution = solve_part1(test_input)
    print(f"Part 1 solution (test): {part1_solution}")

    # Solve Part 2 with test data
    part2_solution = solve_part2(test_input)
    print(f"Part 2 solution (test): {part2_solution}")

def main():
    # Read the input file
    with open('input.txt', 'r') as file:
        data = file.read().strip()

    # Solve Part 1
    part1_solution = solve_part1(data)
    print(f"Part 1 solution: {part1_solution}")

    # Solve Part 2
    part2_solution = solve_part2(data)
    print(f"Part 2 solution: {part2_solution}")

if __name__ == '__main__':
    test()  # Run the test function
    main()