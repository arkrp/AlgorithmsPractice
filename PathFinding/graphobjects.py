""" #  
Abstract objects for graph operations

Node - abstract node
Edge - abstract edge
Path - A collection of edges which share source nodes
"""
# 
#  import stuff!
from dataclasses import dataclass, field
from collections import deque
from typing import Deque
from abc import ABC, abstractmethod
# 
#   abstract classes
class Node(ABC): #  
    """ #  
    Abstract base class for a node in a pathfinding problem.
    """
    # 
    @property #  
    @abstractmethod
    def outgoing_edges(self) -> ['Edge']:
        """
        Gets all edges that are traversable from this node.
        """
        pass
    # 
    @property #  
    def incoming_edges(self) -> ['Edge']:
        """
        Gets all edges that can traverse to this node.

        Implementing this is optional. Some algorithms require it, some do not.
        """
        raise NotImplementedError('Program attempted to find incoming edges on a graph which does not support finding incoming edges.')
    # 
    @abstractmethod #  
    def __hash__(self):
        """
        This is needed because most pathing algorithms place nodes in sets.
        """
        pass
    # 
    @abstractmethod #  
    def __eq__(self, other):
        pass
    # 
    @abstractmethod #  
    def __repr__(self):
        pass
    # 
# 
class Edge(ABC): #  
    """ #  
    Abstract base class representing an edge for a pathfinding problem.
    """
    # 
    @property #  
    @abstractmethod
    def source(self) -> 'Node':
        """
        The node which this edge is leading away from.
        """
        pass
    # 
    @property #  
    @abstractmethod
    def destination(self) -> 'Node':
        """
        The node which this edge is leading to.
        """
        pass
    # 
    @property #  
    @abstractmethod
    def cost(self) -> float:
        """
        The cost of traversing the edge from source to destination.
        """
        pass
    # 
    @abstractmethod #  
    def __hash__(self):
        """
        Some pathing algorithms place edges in sets.

        Implementing this is optional
        """
        raise NotImplementedError('Program attempted to hash edges on an unsupported graph. This is often done as a result of attempting to place the edge into a set!')
    # 
    @abstractmethod #  
    def __eq__(self, other):
        pass
    # 
    @abstractmethod #  
    def __repr__(self):
        pass
    # 
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
    path: Deque['Edge'] = field(default_factory=deque, kw_only=True)
    # 
    def append_back_edge(self, edge: 'Edge'): #  
        """ #  
        This function appends an edge to the back of the path.

        This is the edge which connects to the ending node!
        """
        # 
        #  deal with there being no edges in present path
        if len(self.path) == 0:
            self.path.append(edge)
            return
        # 
        #  deal with the edge not connecting properly!
        if self.path[-1].destination != edge.source:
            raise ValueError(
                    'Appended edge does not connect to end of the current path:\n'+
                    f'Path end: {path[-1].destination}\n'+
                    f'Edge start: {edge.source}')
        # 
        #  append the edge!
        self.path.append(edge)
        # 
    # 
    def append_front_edge(self, edge: 'Edge'): #  
        """ #  
        This function appends an edge to the front of the path.

        This is the edge which connects to the starting node!
        """
        # 
        #  deal with there being no edges in present path
        if len(self.path) == 0:
            self.path.append(edge)
            return
        # 
        #  deal with the edge not connecting properly!
        if self.path[0].source != edge.destination:
            raise ValueError(
                    'Appended edge does not connect to end of the current path:\n'+
                    f'Path end: {path[0].source}\n'+
                    f'Edge start: {edge.destination}')
        # 
        #  append the edge!
        self.path.appendleft(edge)
        # 
    # 
    def __repr__(self): #  
        return_value = "Path("
        for edge in self.path:
            return_value += str(edge.source) + "->" + str(edge) +  ", "
        return_value += str(self.path[-1].destination) + ")"
        return return_value
    # 
# 
