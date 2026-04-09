from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A*

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        front = PriorityQueueFrontier()
        front.add(root, root.cost + grid.h(root.state))

        while True:
            # stop if frontier is empty
            if front.is_empty():
                return NoSolution(reached)
            
            node = front.pop()

            # Check if node is already a solution
            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                result = grid.result(node.state, action)
                cost = node.cost + grid.individual_cost(node.state, action)

                # A node is discarded only when its state has already been reached 
                # with a path cost less than or equal to.
                if (result not in reached) or (cost < reached[result]):
                    node_2 = Node("", result, cost, node, action)
                    reached[result] = cost
                    front.add(node_2, node_2.cost +  grid.h(node_2.state))
