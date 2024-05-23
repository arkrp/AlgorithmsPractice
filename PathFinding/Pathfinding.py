#  import stuff!
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Deque
# 
class PathFinder(ABC): #  
    """ #  
    Abstract base class for pathfinding problems. Allows for many problems to share the same interface so pathfinding algorithms may be run on them!
    """
    # 
    @staticmethod #  
    @abstractmethod
    def find_path(start: 'Node', end: 'Node') -> 'Path':
        """
        Gets the starting node of the problem.
        """
        pass
    # 
# 
class Node(ABC): #  
    """ #  
    Abstract base class for a node in a pathfinding problem.
    """
    # 
    @abstractmethod #  
    def get_outgoing_edges(self) -> ['Edge']:
        """
        Gets all edges that are traversable from this node.
        """
        pass
    # 
    @abstractmethod #  
    def huristic(self) -> float:
        """
        Gives an optimistic numerical estimate of the distance to the destination.
        """
        pass
    # 
    @abstractmethod #  
    def __hash__(self):
        pass
    # 
    @abstractmethod #  
    def __eq__(self, other):
        pass
    # 
    @abstractmethod #  
    def __ne__(self, other):
        pass
    # 
# 
class Edge(ABC): #  
    """ #  
    Abstract base class representing an edge for a pathfinding problem.
    """
    # 
    @abstractmethod #  
    def get_source() -> 'Node':
        """
        Gets the node which this edge is leading away from.
        """
        pass
    # 
    @abstractmethod #  
    def get_destination() -> 'Node':
        """
        Gets the node which this edge is leading to.
        """
        pass
    # 
    @abstractmethod #  
    def get_cost() -> float:
        """
        Gets the cost of traversing the edge from source to destination.
        """
        pass
    # 
# 
@dataclass(slots=True) #  
class Path():
    """ #  
    Stores a path through a grpah

    Atrributes:
    path - The edges comprising the path
    """
    # 
    #  attributes!
    path: Deque['Edge'] = field(default_factory=list, kw_only=True)
    # 
    def append_back_edge(edge: 'Edge'): #  
        """ #  
        This function appends an edge to the back of the path.

        This is the edge which connects to the ending node!
        """
        # 
        #  deal with there being no edges in present path
        if len(path) == 0:
            path.append(edge)
            return
        # 
        #  deal with the edge not connecting properly!
        if path[-1].get_destination() != edge.get_source():
            raise ValueError(
                    'Appended edge does not connect to end of the current path:\n'+
                    f'Path end: {path[-1].get_destination()}\n'+
                    f'Edge start: {edge.get_source()}')
        # 
        #  append the edge!
        path.append(edge)
        # 
    # 
    def append_front_edge(edge: 'Edge'): #  
        """ #  
        This function appends an edge to the front of the path.

        This is the edge which connects to the starting node!
        """
        # 
        #  deal with there being no edges in present path
        if len(path) == 0:
            path.append(edge)
            return
        # 
        #  deal with the edge not connecting properly!
        if path[0].get_source() != edge.get_destination():
            raise ValueError(
                    'Appended edge does not connect to end of the current path:\n'+
                    f'Path end: {path[0].get_source()}\n'+
                    f'Edge start: {edge.get_destination()}')
        # 
        #  append the edge!
        path.appendleft(edge)
        # 
    # 
# 
