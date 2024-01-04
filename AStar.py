import queue

from Node import Node

class AStar(object):

    """
    This is the constructor. It initializes the variables, for modularity
    heuristic function is passed in as a variable
    """
    def __init__(self, root = None, goal = None, heuristic_function = None, cost_per_action = 1):
        self.action_cost = cost_per_action
        self.nodes_created = 1
        self.depth = 0
        self.path = []
        if heuristic_function is None:
            self.heuristic_function = self.stub()
        else:
            self.heuristic_function = heuristic_function
        if root is None:
            self.root = Node([8, 7, 6, 5, 4, 3, 2, 1, 0], cost = 0,
                             heuristic = heuristic_function([8, 7, 6, 5, 4, 3, 2, 1, 0]),
                             zero_at = 8)
        else:
            self.root = root
        self.root.cost = 0
        if goal is None:
            self.goal = Node([0, 1, 2, 3, 4, 5, 6, 7, 8], zero_at = 0)
        else:
            self.goal = goal

    """
    This is the A* implementation. It is the same as psudocode, but instead of using arrays or
    strings to store in explored hashset, it uses ints. Also F(n) is brought outside of the
    Node class to lighten the load on the memory, and paing for it in processing time.
    g(n) is still stored in the Node class.
    """
    def main_body(self):
        # Initialize frontier and explored nodes hashset.
        frontier = queue.PriorityQueue()
        explored_set = set()
        frontier.put((self.Fn(self.root), self.root))

        while not frontier.empty():
            # get the next node in frontier with the least F(n).
            current_node = frontier.get()[1]
            # Goal test.
            if current_node == self.goal:
                # If check passed the save the statistics (exit_function) and exit.
                self.nodes_created = len(explored_set) + len(frontier.queue)
                self.exit_function(current_node)
                explored_set.clear()
                return True
            # If check failed then get children
            children = self.explore_node(current_node)
            # add current node to the explored hashset
            explored_set.add(int(current_node))
            # and add children to the frontier
            for child in children:
                # only if they are not duplicates.
                if child not in explored_set:
                    # If the child is a new never seen node then
                    # update the cost and store it in children node
                    child.cost = current_node.cost + self.action_cost
                    # update the heuristic function (not nessesary)
                    child.heuristic = self.heuristic_function(child.state)
                    # store into the frontier with F(n) values as the priority.
                    frontier.put((self.Fn(child), child))
        return False

    """
    A helper function that explores the nodes.
    """
    def explore_node(self, node):
        actons = node.actions
        children = []
        for action in actons:
            children.append(node.take_action(action))
        return children

    """
    Helper function that does F(n) = g(n) + h(n)
    """
    def Fn(self, node):
        return node.cost + self.heuristic_function(node.state);


    """
    A helper function that colects statistics when goal is reached.
    """
    def exit_function(self, node = None):
        while type(node) == Node:
            self.path.insert(0, node)
            node = node.predecessor
            self.depth += 1
        self.depth -= 1

    def stub(self):
        return -1

    """
    A basic to_string method.
    """
    def __str__(self):
        result = ""
        for i in range(len(self.path)):
            result += "Action: " + str(self.path[i].predecessor_action) + "\n" + str(self.path[i]) + "\n"
        result += "Depth: " + str(self.depth)
        result += "\nNumber of nodes created: " + str(self.nodes_created)
        if len(self.path) > 0:
            result += "\nCost: " + str(self.path[-1].cost)
        return result