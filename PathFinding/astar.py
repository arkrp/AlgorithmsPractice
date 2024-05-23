from .problem import NodePathFindingProblem, PathFindingNode, PathFindingSolution as Problem, Node, Solution
from ..DataStructures.heap import Heap
from dataclasses import dataclass
def a_star(problem: Problem) -> Solution:
    unvisited = Heap()
    visited = set()
    solution = Solution()
    starting_node = problem.get_starting_node()
    unvisited.push(_node_with_distance(starting_node, 0))
    while(True):
        

    return None
@dataclass
class _node_with_distance():
    distance: int
    node: Node
if __name__ == '__main__':
    print('the test procedure for pathfinding algoirthms is not currently implemented')
