def solve_part1(data):
    # First part solution
    """
    A : Rock
    B : Paper
    C : Scissors

    X : Rock
    Y : Paper
    Z : Scissors

    Shape selected : 
    1 : Rock
    2 : Paper
    3 : Scissors

    Outcome of the round : 
    0 : Lost
    3 : Draw
    6 : Won

    Rock < Paper 
    Paper < Scissors
    Scissors < Rock

    Score = Shape + Outcome
    """
    out = {'AY': 6, 'BZ': 6, 'CX': 6, 'AX': 3, 'BY': 3, 'CZ': 3, 'BX': 0, 'CY': 0, 'AZ': 0}
    # The 'out' dictionary represents the outcomes for each combination of ennemy_hand + my_hand.

    guide = data.split('\n')
    score = 0

    for elt in guide:
        ennemy_hand, my_hand = elt.split()
        # Split the combination into ennemy_hand and my_hand.

        shape = 'XYZ'.index(my_hand) + 1
        # Get the index of my_hand in the string 'XYZ' and add 1 to it to get the shape value.

        outcome = out[ennemy_hand + my_hand]
        # Get the outcome value from the 'out' dictionary based on the ennemy_hand and my_hand combination.

        score += shape + outcome
        # Add the shape value and outcome value to the score.

    return score


def solve_part2(data):
    # Second part solution
    """
    X : Loose
    Y : Draw
    Z : Win
    """
    out = {'AY': 4, 'BZ':9 , 'CX': 2, 'AX': 3, 'BY': 5, 'CZ': 7, 'BX':1, 'CY':6, 'AZ':8 }

    guide = data.split('\n')
    score = 0

    for elt in guide:
        enemy_hand, my_hand = elt.split() # 'B Z' -> ['B','Z']
        score += out[enemy_hand+my_hand]

    return score

def test():
    # Test data
    test_input = """A Y
B X
C Z"""
    
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