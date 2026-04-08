from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = {}

        # Initialize frontier with the root node
        front = StackFrontier()
        front.add(root)
        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        while True:
            # stop if frontier is empty
            if front.is_empty(): 
                return NoSolution(expanded)   
            
            node = front.remove()

            #control que evita expandir un estado ya expandido
            if node.state in expanded: continue
            expanded[node.state] = True

            for action in grid.actions(node.state):
                result = grid.result(node.state, action)

                #add a child
                if result not in expanded:
                    node_2 = Node("", result, node.cost + grid.individual_cost(node.state, action), node, action)
                    
                    # Check if the child is a solution
                    if grid.objective_test(result):
                        print("Expanded:", len(expanded))
                        return Solution(node_2, expanded)
                    
                    front.add(node_2)
                    

        return NoSolution(expanded)