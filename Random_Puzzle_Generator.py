import random

"""
This function generates a random 8 puzzle and checks if it is valid.
Repeats if check failed.
"""
def get_solvable_puzzle():
    puzzle = random_puzzle()
    while not test_puzzle(puzzle):
        puzzle = random_puzzle()
    return puzzle

"""
This function generates a random 8 puzzle. 
Does nor guarantee that the puzzle is solvable
"""
def random_puzzle():
    result = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    i = 0
    while i < 9:
        pos = random.randrange(9)
        if result[pos] == -1:
            result[pos] = i
            i += 1
    return result


"""
This function tests if the * puzzle is solvable
"""
def test_puzzle(puzzle):
    inversions = 0
    for i in range(8):
        for j in range(i+1, 9):
            if puzzle[i] > puzzle[j] and puzzle[j] != 0:
                inversions += 1
    if inversions % 2 == 0:
        return True
    else :
        return False

"""
This function does additional tests for manually entered puzzle
along the regular solvability check
"""
def test_manual_input(puzzle):
    if len(puzzle) != 9:
        return False
    for i in range(9):
        if get_position(puzzle, i) == -1:
            return False
    return test_puzzle(puzzle)

"""
A helper function that gets the location of a 
numbered tile in the puzzle
"""
def get_position(puzzle, value):
    position = -1
    for i in range(len(puzzle)):
        if puzzle[i] == value:
            position = i
    return position