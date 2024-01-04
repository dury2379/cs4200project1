class Node(object):

    """ this is a constructor that initializes all the values. It has alot of defaulst"""
    def __init__(self, state = [], predecessor = None, action = None, cost = -1, heuristic = -1, zero_at = -1):
        self.state = state
        self.predecessor = predecessor
        self.predecessor_action = action
        self.cost = cost
        self.heuristic = heuristic
        if zero_at == -1:
            self.zero_position = self.get_position(0)
        else:
            self.zero_position = zero_at
        self.actions = self.get_actions()


    """ 
    This method get all possible actions. It gets the location of the 0 tile
    and testing where it can move to.
    """
    def get_actions(self):
        result = []

        if self.zero_position == -1:
            return result

        if self.zero_position % 3 != 0:
            result.append(chr(108)) # 108 - l aka left

        if (self.zero_position + 1) % 3 != 0:
            result.append(chr(114)) # 114 - r aka right

        if self.zero_position < 6:
            result.append(chr(100)) # 100 - d aka down

        if self.zero_position > 2:
            result.append(chr(117)) # 117 - u aka up

        return result

    """
    This method recives the action from the programm above and creates a childnode.
    It swaps the 0 tile with another tile, saves this node as parant of the childnode
    and stores the action in childnode.
    """
    def take_action(self, action):
        if action not in self.actions:
            print("Invalid action")
            return None

        if action == "u":
            return Node(self.swap(self.state.copy(), self.zero_position, self.zero_position - 3),
                         predecessor = self, action = chr(117), zero_at = self.zero_position - 3)
        if action == "d":
            return Node(self.swap(self.state.copy(), self.zero_position, self.zero_position + 3),
                         predecessor = self, action = chr(100), zero_at = self.zero_position + 3)
        if action == "l":
            return Node(self.swap(self.state.copy(), self.zero_position, self.zero_position - 1),
                         predecessor = self, action = chr(108), zero_at = self.zero_position - 1)
        if action == "r":
            return Node(self.swap(self.state.copy(), self.zero_position, self.zero_position + 1),
                         predecessor = self, action = chr(114), zero_at = self.zero_position + 1)
    """
    A helper function that returns the position of a tile.
    """
    def get_position(self, value):
        position = -1
        for i in range(len(self.state)):
            if self.state[i] == value:
                position = i
        return position

    def swap(self, list, p1, p2):
        temp  = list[p1]
        list[p1] = list[p2]
        list[p2] = temp
        return list

    def get_zero_location(self):
        return get_position(0)

    """
    In this implementation of A* explored_nodes hashset stores nodes in form of a 
    single int value. Because 8 puzzle only uses 9 digits, every combination of
    8 puzzle is a unique integer value. Where first 3 digits is the top row, next 3 
    is the second row, last 3 is the bottom row. This allows A* to do arithmetics
    on the nodes, so I overloaded some arithmetic operators to utilize this
    property.
    """
    def __eq__(self, other):
        return self.__int__() == other

    def __gt__(self, other):
        return self.__int__() > other

    def __lt__(self, other):
        return self.__int__() < other

    def __int__(self):
        result = 0
        for i in self.state:
            result = result * 10 + i
        return int(result)

    def __hash__(self):
        return hash(self.__int__())
    """
    Basic to_string method for printouts.
    """
    def __str__(self):
        result = ""
        for i in range(len(self.state)):
            result += str(self.state[i])
            if i % 3 == 2:
                result += "\n"
            else:
                result += " "
        return result