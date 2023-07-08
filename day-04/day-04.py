def solve_part1(data):
    # First part solution
    count = 0
    sections = data.split('\n')
    # Seperate each duos (lines)

    for elt in sections : 

        first, second = elt.split(',')
        # For each duos, split the first and second elf

        first_range = range(int(first.split('-')[0]), int(first.split('-')[1])+1)
        # Get the range of the first elf
        second_range = range(int(second.split('-')[0]), int(second.split('-')[1])+1)
        # the range of the second elf

        # If their intersection is equal to the range
        if (set(first_range) & set(second_range)) == set(first_range) \
        or (set(first_range) & set(second_range)) == set(second_range):
            count += 1

    return count

def solve_part2(data):
    # Second part solution

    count = 0
    sections = data.split('\n')

    for elt in sections : 
        first, second = elt.split(',')
        first_range = range(int(first.split('-')[0]), int(first.split('-')[1])+1)
        second_range = range(int(second.split('-')[0]), int(second.split('-')[1])+1)
        if (set(first_range) & set(second_range)) :
            count += 1
            
    return count

def test():
    # Test data
    test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    
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