def solve_part1(data):
    # First part solution
    # uppercase -38 and lowercase -96
    priority = 0
    rucksack = data.split('\n')

    for elt in rucksack : 
        first, second = elt[:int(len(elt)/2):], elt[int(len(elt)/2)::]
        intersection = [set(first) & set(second)][0]
        item = next(iter(intersection)) # Get the first item in set
        if item.isupper() :
            priority += ord(item) - 38
        else:
            priority += ord(item) - 96
    return priority


def solve_part2(data):
    # Second part solution
    priority = 0
    rucksack = data.split('\n')

    for i in range(0, len(rucksack), 3):
        first, second, third = rucksack[i], rucksack[i+1], rucksack[i+2]
        intersection = set(first) & set(second) & set(third)
        item = next(iter(intersection))
        if item.isupper() :
            priority += ord(item) - 38
        else:
            priority += ord(item) - 96
    return priority


def test():
    # Test data
    test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    
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