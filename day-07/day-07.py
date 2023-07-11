def solve_part1(data):
    # First part solution
    path = '/'
    dirs = {'/':0}
    lines = data.split('\n')
    for l in lines :
        s = l.split()

        if s[0] == '$':
            # If it's a command line

            if s[1] == 'cd':
                # Manage changing directory

                if s[2] == '/':
                    # Going back to the outermost
                    path = '/'

                elif s[2] == '..':
                    # Going back in directory
                    path = path[:path.rfind('/')]

                else:
                    # Add the current directory to path
                    path += '/'  + s[2]
                    dirs.update({path:0})
        
        elif s[0] == 'dir':
            pass

        else:
            # Update size for every directory
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += int(s[0])
                dir = dir[:dir.rfind("/")]

    condition = [dirs[elt] for elt in dirs if dirs[elt]< 100000]
    return sum(condition)


def solve_part2(data):
    # Second part solution
    path = '/'
    dirs = {'/':0}
    lines = data.split('\n')
    for l in lines :
        s = l.split()

        if s[0] == '$':
            if s[1] == 'cd':
                if s[2] == '/':
                    path = '/'
                elif s[2] == '..':
                    path = path[:path.rfind('/')]
                else:
                    path += '/'  + s[2]
                    dirs.update({path:0})    

        elif s[0] == 'dir':
            pass

        else:
            dir = path
            for i in range(path.count("/")):
                dirs[dir] += int(s[0])
                dir = dir[:dir.rfind("/")]
    
    x = 30000000 - (70000000 - dirs["/"])
    condition = [dirs[elt] for elt in dirs if dirs[elt] >= x]
    return min(condition)
    

def test():
    # Test data
    test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    
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