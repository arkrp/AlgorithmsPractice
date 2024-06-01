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
from typing import Any
from .graphobjects import Node, Edge
from .pathfinder import GoalCondition
# 
#   typing!
NodeId = Any
EdgeId = Any
# 
#   classes
@dataclass #  
class FiniteGraph():
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
        #  check argument validity
        if edge_id in self.edge:
            raise ValueError(f"Attempted to insert edge with id which is already taken! {edge_id=}")
        # 
        #  create the source and destination nodes if needed!
        if (source_id not in self.node):
            self.add_node(source_id)
        if (destination_id not in self.node):
            self.add_node(destination_id)
        # 
        #  configure the edge!
        self.edge[edge_id] = FiniteEdge(edge_id, self)
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
        #  check argument validity
        if edge_id not in self.edge:
            raise ValueError(f"Attempted to remove an edge which is not present {edge_id=}")
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
@dataclass(frozen=True) #  
class FiniteNode(Node):
    #  attributes!
    node_id: NodeId = field()
    graph: FiniteGraph = field(hash=False ,repr=False, compare=False)
    # 
    @property #  
    def outgoing_edges(self) -> [Edge]:
        """
        Gets all edges that are traversable from this node.
        """
        return [self.graph.edge[i] for i in self.graph.outgoing_edges[self.node_id]]
    # 
    @property #  
    def incoming_edges(self) -> [Edge]:
        """
        Gets all edges that can traverse to this node.
        """
        return [self.graph.edge[i] for i in self.graph.incoming_edges[self.node_id]]
    # 
# 
@dataclass(frozen=True) #  
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
def parse_edge_list(edge_list: [[NodeId, NodeId, float]]): #  
    """
    Turns a list of unnammed edges into a graph
    
    each entry in the edge list represents an edge. It is formatted as:
    [source node id, destination node id, edge cost]

    an example input would look like this!
    [[1,2,1],[2,3,1.1],[3,1,1.2],[1,1,0.5]]
    this represents a graph which has the following edges!
    1 -> 2 cost 1
    2 -> 3 cost 1.1
    3 -> 1 cost 1.2
    1 -> 1 cost 0.5
    """
    return_graph = FiniteGraph()
    for edge_info_and_number in zip(edge_list, range(len(edge_list))):
        edge_info, edge_number = edge_info_and_number
        source_id, destination_id, cost = edge_info
        return_graph.add_edge(edge_number, source_id, destination_id, cost)
    return return_graph
# 
def id_goal_condition(node_ids: set[NodeId]): #  
    """ #  
    Generates a GoalCondition which is true only for nodes with specific node_id attributes
    """
    # 
    class LookForId(GoalCondition): #  
        @staticmethod
        def is_goal(node):
            if node.node_id in node_ids:
                return True
            return False
    # 
    return LookForId
# 
#  testing!
if __name__ == '__main__':
    print('Starting test (Not Automatic, please visually inspect)')
    edge_list = [
        [1,2,10],
        [2,3,11],
        [3,1,12],
        [1,1,13]
        ]
    print(f'Parsing edge list: {edge_list}')
    my_graph = parse_edge_list(edge_list)
    print('Generated graph:')
    print(f'{my_graph.outgoing_edges=}')
    print(f'{my_graph.incoming_edges=}')
    print(f'{my_graph.node.keys()=}')
    print(f'{my_graph.edge.keys()=}')
    print(f'{my_graph.edge_source=}')
    print(f'{my_graph.edge_destination=}')
    print(f'{my_graph.edge_cost=}')
    print('Generated responses:')
    print(f'{my_graph.edge[0].source=}')
    print(f'{my_graph.edge[0].destination=}')
    print(f'{my_graph.edge[0].cost=}')
    print(f'{my_graph.node[1].outgoing_edges=}')
    print(f'{my_graph.node[1].incoming_edges=}')
    
# 
