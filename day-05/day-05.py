import re
import copy

def solve_part1(data, stack):
    # First part solution
    stack1 = copy.deepcopy(stack)
    
    procedure = data.split('\n')
    for elt in procedure : 
        quantity, from_stack, to_stack = [int(digit) for digit in re.findall(r'\d+', elt)]

        for i in range(quantity):
            stack1[to_stack -1] += stack1[from_stack - 1][-1:]
            # += to add a list to a list

            del stack1[from_stack -1][-1:]
    
    output = ''
    for elt in stack1 :
        output += elt[:][-1]

    return output

def solve_part2(data, stack):
    # Second part solution
    stack2 = copy.deepcopy(stack)

    procedure = data.split('\n')
    for elt in procedure : 
        quantity, from_stack, to_stack = [int(digit) for digit in re.findall(r'\d+', elt)]
        stack2[to_stack -1] += stack2[from_stack - 1][-quantity:]
        del stack2[from_stack - 1][-quantity:]
    
    output = ''
    for elt in stack2 :
        output += elt[:][-1]

    return output


def test():
    # Test data
    test_input = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    stack = [['Z','N'],
             ['M','C','D'],
             ['P']]
    

    # Solve Part 1 with test data
    part1_solution = solve_part1(test_input, stack)
    print(f"Part 1 solution (test): {part1_solution}")

    # Solve Part 2 with test data
    part2_solution = solve_part2(test_input, stack)
    print(f"Part 2 solution (test): {part2_solution}")

def main():
    # Read the input file
    with open('input.txt', 'r') as file:
        data = file.read().strip()
    stack = [
        ['S','T','H','F','W','R'],
        ['S','G','D','Q','W'],
        ['B','T','W'],
        ['D','R','W','T','N','Q','Z','J'],
        ['F','B','H','G','L','V','T','Z'],
        ['L','P','T','C','V','B','S','G'],
        ['Z','B','R','T','W','G','P'],
        ['N','G','M','T','C','J','R'],
        ['L','G','B','W']
    ]
    # Solve Part 1
    part1_solution = solve_part1(data, stack)
    print(f"Part 1 solution: {part1_solution}")

    # Solve Part 2
    part2_solution = solve_part2(data, stack)
    print(f"Part 2 solution: {part2_solution}")

if __name__ == '__main__':
    test()  # Run the test function
    main()