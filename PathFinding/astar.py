""" #  
Contains the AStar pathfinder.

This pathfinder is a tunable general purpose pathfinding algorithm.

classes
AStar - a pathfinding.Pathfinder which allows for general purpose pathfinding.
"""
# 
#  import stuff
from .pathfinder import ShortestPathfinder, GoalCondition, Hueristic, NullHueristic, NoPathError
from .graphobjects import Node, Path, Edge
from ..DataStructures.heap import Heap
from dataclasses import dataclass, field
# 
class AStar(ShortestPathfinder): #  
    """ #  
    Wrapper for A-Star pathfinding algorithm

    The A-Star pathfinding algorithm is a modification of Dijkstra's algorithm which allows for the node priority to be arbitrarily biased. By tuning these biases properly A star can run faster than Djikstra's without loss of the ability to find the shortest path

    If no hueristic is provided, this algorithm is equivilant to Dijkstra's algorithm.

    example usage:
        shortest_path = AStar.find_path(start_node, goal_condition, hueristic=hueristic)

    Warning! - if any of the starting nodes meet the goal condition this will return an empty path.
    """
    # 
    @staticmethod #  
    def find_path(starting_nodes: [Node], goal_condition: GoalCondition, *, hueristic: Hueristic=NullHueristic) -> Path:
        """ #  
        A Star pathfinding algorithm

        Finds the shortest path from any starting node to a node which meets the goal condition.

        starting_nodes - The list of all nodes which the path may start from
        goal_condition - A \'pathfinder.GoalCondition\' which tells us when we have reached our goal
        hueristic - A \'pathfinder.Hueristic\' which biases our distance estimates to make the algorithm run faster.

        If no hueristic is provided, this algorithm is equivilant to Dijkstra's algorithm.

        Warning! - if any of the starting nodes meet the goal condition this will return an empty path.
        """
        # 
        #  declare data structures
            #stores the places we have seen an edge to and are yet to explore
        unexplored = Heap()
            #stores all the places we have explored
        explored = set()
            #stores the optimal edge leading to each node
        discovering_edge: dict[Node, Edge] = dict()
            #stores the shortest distance to each node
        minimum_distance: dict[Node, float] = dict()
        # 
        #  declare state variables!
            #records whether we have found a path to our destination
        path_found = False
            #records the final node of our path to the destination
        path_final_node = None
        # 
        #  define exploration functions
        def explore_node(node: Node): #  
            """ #  
            finds the outgoing edges of a node and adds them to the exploration list
            """
            # 
            #  record that we have explored this node
            explored.add(node)
            # 
            #  deal with reaching our destination!
            if goal_condition.is_goal(node):
                nonlocal path_found
                nonlocal path_final_node
                path_found = True
                path_final_node = node
                return
            # 
            #  add all outgoing edges to our list of things to explore!
            outgoing_edges = node.outgoing_edges
            for edge in outgoing_edges:
                unexplored.push(_exploration_vector(
                    edge,
                    minimum_distance[edge.source]+
                    edge.cost+
                    hueristic.hueristic(edge.destination)
                    ))
            # 
        # 
        def explore_edge(edge: Edge):
            """ #  
            Explores an edge

            Exploring an edge checks if the edge's destination node is explored. If the node hasn't been explored yet then we do the following three things:
            1. register the edge as the discovering edge of the node
            2. record the minimum distance to the node
            3. explore the node!
            """
            # 
            #  deal with the destination node already being explored
            if edge.destination in explored:
                return
            # 
            #  record path information about the destination
            discovering_edge[edge.destination] = edge
            minimum_distance[edge.destination] = edge.cost + minimum_distance[edge.source]
            # 
            #  explore the destination!
            explore_node(edge.destination)
            # 
        # 
        #  initialize values for starting nodes!
        for node in starting_nodes:
            discovering_edge[node] = None
            minimum_distance[node] = 0
        # 
        #   explore all starting nodes
        for node in starting_nodes:
            explore_node(node)
        # 
        #  explore until we reach our destination!
        while not (path_found or unexplored.is_empty()):
            #  get our edge!
            vector = unexplored.pop()
            edge = vector.edge
            # 
            #  explore the edge!
            explore_edge(edge)
            # 
        # 
        #  deal with no path existing
        if not path_found:
            raise NoPathError('Pathfinding algorithm found no path from source to destination')
        # 
        #  construct the optimal path from the information we aquired!
        path = Path()
        current_node = path_final_node
        while discovering_edge[current_node] != None:
            path.append_front_edge(discovering_edge[current_node])
            current_node = discovering_edge[current_node].source
        return path
        # 
    # 
# 
@dataclass(order=True) #  
class _exploration_vector():
    """
    represents an edge, and its priority in the priority queue.
    """
    # The edge we wish to explore
    edge: Edge = field(compare=False)
    # the priority of the edge. Computed as distance of destination node,
    bias: float = field(compare=True)
# 
#  testing!
if __name__ == '__main__':
    from .test import basic_pathfinder_test
    basic_pathfinder_test(AStar)
    from .test import no_path_pathfinder_test
    no_path_pathfinder_test(AStar)
# 
