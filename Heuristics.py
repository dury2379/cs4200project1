
"""
A separate implementation of the heuristics function.
This is manhattan distance sum. It calculates delta_x and
delta_y foreach numbered tile and summs it up.
"""
def manhattan_distance(state):
    sum = 0
    for i in range(1, len(state)):
        dx = abs((i % 3) - (loaction_of(state, i) % 3))
        dy = abs(int(i / 3) - int(loaction_of(state, i) / 3))
        sum += dx + dy
    return sum

"""
A simple heuristic function. If it is not in the
 right place, increase cout.
"""
def missplaced_tiles(state):
    sum = 0
    for i in range(1, len(state)):
        if state[i] != i:
            sum += 1
    return sum

def loaction_of(state, value):
    for i in range(len(state)):
        if state[i] == value:
            return i
    return -1