from abc import ABC, abstractmethod
from dataclasses import dataclass
class NodePathFindingProblem(ABC): #f
    """ #f
    Abstract base class for pathfinding problems. Allows for many problems to share the same interface so pathfinding algorithms may be run on them!
    """
    #d
    @abstractmethod #f
    def get_starting_node() -> PathFindingNode:
        """
        gets the starting node
        """
        pass
    #d
    @abstractmethod #f
    def is_end_node() -> bool:
        """
        determines if a node is the destination node
        """
        pass
    #d
#d
class PathFindingNode(ABC): #f
    """ #f
    Abstract base class for a node in a pathfinding problem. Allows for nodes 
    """
    #d
    @abstractmethod #f
    def get_outgoing_edges(self) -> [PathFindingEdge]:
        """
        Gets all edges that are traversable from this node.
        """
        pass
    #d
    @abstractmethod #f
    def huristic(self) -> float:
        """
        Gives an optimistic numerical estimate of the distance to the destination.
        """
        pass
    #d
    @abstractmethod #f
    def __hash__(self):
        pass
    #d
    @abstractmethod #f
    def __eq__(self, other):
        pass
    #d
#d
class PathFindingEdge(ABC): #f
    """ #f
    Abstract base class representing an edge for a pathfinding problem.
    """
    #d
    @abstractmethod #f
    def get_source() -> PathFindingNode:
        """
        Gets the node which this edge is leading away from.
        """
        pass
    #d
    @abstractmethod #f
    def get_destination() -> PathFindingNode:
        """
        Gets the node which this edge is leading to.
        """
        pass
    #d
    @abstractmethod #f
    def get_cost() -> float:
        """
        Gets the cost of traversing the edge from source to destination.
        """
        pass
    #d
#d
@dataclass(slots=True) #f
class PathFindingSolution:
    """ #f
    stores the solution to a pathfinding problem
    """
    #d
    path: [PathFindingNode]
    cost: float
#d
    
