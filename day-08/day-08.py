def solve_part1(data):
    # First part solution
    visible = 0
    data = [[int(elt) for elt in line ] for line in data.split('\n')]
    col = len(data[0])
    row = len(data)

    # 4 overlaps
    edges = (row*2) + ((col-2)*2)
    visible += edges

    for i in range(1,row - 1):
        for j in range(1,col - 1):
            left = [data[i][j-x] for x in range(1, j + 1)]
            right = [data[i][j+x] for x in range(1, col - j)]
            up = [data[i-x][j] for x in range(1, i + 1)]
            down = [data[i+x][j] for x in range(1, row - i)]

            if max(left)<data[i][j] or max(right)<data[i][j] or max(up)<data[i][j] or max(down)<data[i][j]:
                visible += 1
                
    return visible

def solve_part2(data):
    # Second part solution

    data = [[int(elt) for elt in line ] for line in data.split('\n')]
    col = len(data[0])
    row = len(data)

    scores = [] 

    for i in range(1,row - 1):
        for j in range(1,col - 1):
            left = [data[i][j-x] for x in range(1, j + 1)]
            right = [data[i][j+x] for x in range(1, col - j)]
            up = [data[i-x][j] for x in range(1, i + 1)]
            down = [data[i+x][j] for x in range(1, row - i)]

            scenic_score = 1
            for elt in [left, right, up, down]:
                score = 0
                for k in range(len(elt)):
                    if elt[k] < data[i][j]:
                        score += 1
                    else:
                        score += 1
                        break
                scenic_score *= score
            
            scores.append(scenic_score)
    
    return max(scores)


def test():
    # Test data
    test_input = """30373
25512
65332
33549
35390"""
    
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
