""" #  
A finite representation of a graph.

This allows for basic pathfinding and other graph operations to be performed!

FiniteGraph - A representation of a finite graph contained entirely in memory.
FiniteNode - A node which comprises a FiniteGraph
FiniteEdge - An edge wich connects the nodes in a FiniteGraph
"""
# 
#  todo list
#TODO make public dictionary accesses proxy types!
# 
#  import stuff!
from dataclasses import dataclass, field
from graphobjects import Node, Edge
from typing import Any
# 
#  use typing to make things clear
NodeId = Any
EdgeId = Any
# 
#  basic implementation for simple usage
class FiniteGraph(): #  
    """
    Represents a graph of finite size for pathing

    Please don't write to \'node\' or \'edge\' manually. Read only please.
    """
    #  needed data!
    node: dict[NodeId, Node] = field(default_factory=dict)
    incoming_edges: dict[NodeId, set[EdgeId]] = field(default_factory=dict)
    outgoing_edges: dict[NodeId, set[EdgeId]] = field(default_factory=dict)
    edge: dict[EdgeId, Edge] = field(default_factory=dict)
    edge_source: dict[EdgeId, NodeId] = field(default_factory=dict)
    edge_destination: dict[EdgeId, NodeId] = field(default_factory=dict)
    edge_cost: dict[EdgeId, float] = field(default_factory=dict)
    # 
    def add_node(self, node_id: NodeId): #  
        """ #  
        Places a new node in our graph!
        """
        # 
        #  make sure we aren't inserting a duplicate
        if node_id in self.node:
            raise ValueError(f"Attempted to add a duplicate node {node_id=}")
        # 
        #  initialize the node!
        self.node[node_id] = FiniteNode(node_id, self)
        self.incoming_edges[node_id] = set()
        self.outgoing_edges[node_id] = set()
        # 
    # 
    def remove_node(self, node_id: NodeId): #  
        """ #  
        Removes an existing node!

        Also removes all edges that were connected to that node!
        """
        # 
        #  check argument validity
        if node_id not in self.node:
            raise ValueError(f"Attempted to remove a node which is not present {node_id=}")
        # 
        #  remove all connected edges
        for edge_id in self.incoming_edges[node_id]:
            self.remove_edge(edge_id)
        for edge_id in self.outgoing_edges[node_id]:
            self.remove_edge(edge_id)
        # 
        #  delete the node
        del self.node[node_id]
        del self.incoming_edges[node_id]
        del self.outgoing_edges[node_id]
        # 
    # 
    def add_edge(self, edge_id: EdgeId, source_id: NodeId, destination_id: NodeId, cost: float): #  
        """ #  
        Adds an edge to the graph!

        Creates necissary nodes if they don't already exist!
        """
        # 
        #  create the source and destination nodes if needed!
        if (source_id not in self.node.values):
            self.add_node(source_id)
        if (destination_id not in self.node.values):
            self.add_node(destination_id)
        # 
        #  configure the edge!
        self.edge[edge_id] = Edge(edge_id, self)
        self.edge_source[edge_id] = source_id
        self.edge_destination[edge_id] = destination_id
        self.edge_cost[edge_id] = cost
        # 
        #  connect the edge!
        self.incoming_edges[destination_id].add(edge_id)
        self.outgoing_edges[source_id].add(edge_id)
        # 
    # 
    def remove_edge(edge_id: EdgeId): #  
        """ #  
        Removes an edge
        """
        # 
        #  locate the connected nodes
        source_id: NodeId = self.edge_source[edge_id]
        destination_id: NodeId = self.edge_destination[edge_id]
        # 
        #  disconnect the nodes from the edge
        self.incoming_edges[destination_id].remove(edge_id)
        self.outgoing_edges[source_id].remove(edge_id)
        # 
        #  destroy the edge!
        del self.edge[edge_id]
        del self.edge_source[edge_id]
        del self.edge_destination[edge_id]
        del self.edge_cost[edge_id]
        # 
    # 
# 
@dataclass #  
class FiniteNode(Node):
    #  attributes!
    node_id: Any = field()
    graph: FiniteGraph = field(hash=False ,repr=False, compare=False)
    # 
    def get_outgoing_edges(self) -> [Edge]: #  
        """
        Gets all edges that are traversable from this node.
        """
        return [self.graph.edge[i] for i in self.graph.outgoing_edges[self.node_id]]
    # 
    def get_incoming_edges(self) -> [Edge]: #  
        """
        Gets all edges that can traverse to this node.
        """
        return [self.graph.edge[i] for i in self.graph.incoming_edges[self.node_id]]
    # 
# 
@dataclass #  
class FiniteEdge(Edge):
    #  attributes!
    edge_id: EdgeId = field()
    graph: FiniteGraph = field(hash=False ,repr=False, compare=False)
    # 
    @property #  
    def source(self) -> Node:
        """
        The node which this edge is leading away from.
        """
        edge_id = self.edge_id
        graph = self.graph
        return graph.node[graph.edge_source[edge_id]]
    # 
    @property #  
    def destination(self) -> 'Node':
        """
        The node which this edge is leading to.
        """
        edge_id = self.edge_id
        graph = self.graph
        return graph.node[graph.edge_destination[edge_id]]
    # 
    @property #  
    def cost(self) -> float:
        """
        The cost of traversing the edge from source to destination.
        """
        edge_id = self.edge_id
        graph = self.graph
        return graph.edge_cost[edge_id]
    # 
# 
# 
