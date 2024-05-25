""" #  
Abstract base classes for pathfinding problems through a graph

Multigraphs are not supported.

Contained classes
Pathfinder - abstract function wrapper for find_path(start, end) method.
ShortestPathfinder - Pathfinder which finds the shortest path
GoalCondition - a wrapper class for the function GoalCondition.is_goal. This determines if a certain node is a destination node.
Hueristic - a wrapper class for the function Hueristic.hueristic. This gives a biased estimate for the distance of the node from the solution.
NullHueristic - a hueristic which always returns zero. Eg, zero bias.
"""
# 
#  import stuff!
from abc import ABC, abstractmethod
from .graphobjects import Node, Path
# 
class Pathfinder(ABC): #  
    """ #  
    Abstract base class for pathfinding problems. Allows for many problems to share the same interface so pathfinding algorithms may be run on them!

    Example usage: path = Pathfinder.find_path(starting_node, goal_condition)
    """
    # 
    @staticmethod #  
    @abstractmethod
    def find_path(starting_nodes: [Node], goal_condition: 'GoalCondition') -> Path:
        """
        gets a path from a starting node to a node which meets the goal condition!
        """
        pass
    # 
# 
class ShortestPathfinder(Pathfinder): #  
    """ #  
    Finds the shortest path

    Example usage: path = ShortestPathfinder.find_path(starting_node, goal_condition)
    """
    # 
    pass
# 
class GoalCondition(ABC): #  
    @staticmethod #  
    @abstractmethod
    def is_goal(node: Node) -> bool:
        pass
    # 
# 
class Hueristic(ABC): #  
    @staticmethod #  
    @abstractmethod
    def hueristic(node: Node) -> float:
        pass
    # 
# 
class NullHueristic(Hueristic): #  
    @staticmethod #  
    def hueristic(node: Node) -> float:
        return 0
    # 
# 
