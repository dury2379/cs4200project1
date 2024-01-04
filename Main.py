import time
from Heuristics import manhattan_distance, missplaced_tiles
from Random_Puzzle_Generator import test_manual_input, get_solvable_puzzle
from AStar import AStar
from Node import Node

"""
Separate manual input for an 8 puzzle function.
Works by processing row by row. Alot of input cheking.
"""
def manual_input():
    result = []
    row = 0
    while row < 3:
        row_string = input("Enter row " + str(row + 1) + ": ")
        try:
            if len(row_string.split(" ")) == 3:
                result += [int(i) for i in row_string.split(" ")]
                row += 1
            else:
                print("Invalid")
        except:
                print("Invalid")
    return result

"""
This function automatically generates and solves 100 puzzles,
collects statistics and prints them out. Does not print the 
solutions because printouts take too long and does not reflect 
the efficiency. 
"""
def automated_test(h_function):
    depth = {}
    for i in range(100):
        root = Node(state = get_solvable_puzzle(), cost  = 0)
        A = AStar(root, heuristic_function = h_function)
        start_time = time.time()
        A.main_body()
        if A.depth not in depth:
            depth[A.depth] = {"time": [(time.time() - start_time)], "search cost": [A.nodes_created]}
        else:
            depth[A.depth]["time"].append((time.time() - start_time))
            depth[A.depth]["search cost"].append(A.nodes_created)
    sorted_depth = sorted(depth.keys())
    for i in sorted_depth:
        print("Depth:", i, "Average time:", int(sum(depth[i]["time"]) * 1000 / len(depth[i]["time"])), "Average cost (nodes generated):", sum(depth[i]["search cost"])/len(depth[i]["search cost"]), "Number of tests:", len(depth[i]["time"]))

"""
Main function. Take in mode and heuristic function choise.
Then excecutes the A* algorithm. Prints solutions or statistics.
"""
def main():
    mode = -1
    heuristic = -1
    A = None

    while mode != 1 and mode != 2 and mode != 3:
        print("Choose mode:\n[1] Manually enter the puzzle\n[2] Test 100 random puzzles automatically\n[3] Test one random puzzle automatically")
        mode = int(input())

    while heuristic != 1 and heuristic != 2:
        print("Choose heuristic:\n[1] Manhattan distance\n[2] Misplaced tiles")
        heuristic = int(input())

    if heuristic == 1:
        heuristic_function = manhattan_distance
    else:
        heuristic_function = missplaced_tiles

    if mode == 1:
        root_state = manual_input()
        while not test_manual_input(root_state):
            print("Unsolvable/bad puzzle. Enter again.")
            root_state = manual_input()
        # creating root node
        root = Node(state = root_state, cost = 0)
        # Initializing A*
        A = AStar(root, heuristic_function = heuristic_function)
        # Start time. Used for total time calculation
        start_time = time.time()
        # A.main_body() function does the tree traversing
        A.main_body()
        # End time. Used for total time calculation
        end_time = time.time()
        print(A)
        print("Time:", int((end_time - start_time) * 1000))
    elif mode == 2:
        automated_test(heuristic_function)
    else:
        # creating root node with random solvable state.
        root = Node(state = get_solvable_puzzle(), cost=0)
        # Initializing A*
        A = AStar(root, heuristic_function=heuristic_function)
        # Start time. Used for total time calculation
        start_time = time.time()
        # A.main_body() function does the tree traversing
        A.main_body()
        # End time. Used for total time calculation
        end_time = time.time()
        print(A)
        print("Time:", int((end_time - start_time) * 1000))

main()