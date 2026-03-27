from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """

        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        # Add the root to the front
        front = QueueFrontier()
        front.add(root)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Check if root is already a solution
        if grid.objective_test(root.state):
            return Solution(root, reached)

        while True:
            # stop if frontier is empty
            if front.is_empty(): 
                return NoSolution(reached)

            node = front.remove()

            for action in grid.actions(node.state):
                result = grid.result(node.state, action)

                # Add a child
                if result not in reached:
                    node_2 = Node("", result, node.cost + grid.individual_cost(node.state, action), node, action)
                    
                    # Check if the child is a solution
                    if grid.objective_test(result):
                        return Solution(node_2, reached)
                    
                    # Add child to front
                    reached[result] = True
                    front.add(node_2)
