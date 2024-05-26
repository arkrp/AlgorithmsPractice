""" #  
Contains the AStar pathfinder.

This pathfinder is a tunable general purpose pathfinding algorithm.

classes
AStar - a pathfinding.Pathfinder which allows for general purpose pathfinding.
"""
# 
#  import stuff
from .pathfinder import ShortestPathfinder, GoalCondition, Hueristic, NullHueristic
from .graphobjects import Node, Path, Edge
from ..DataStructures.heap import Heap
from dataclasses import dataclass, field
# 
class AStar(ShortestPathfinder): #  
    """ #  
    Wrapper for A-Star pathfinding algorithm

    The A-Star pathfinding algorithm is a modification of Dijkstra's algorithm which allows for the node priority to be arbitrarily biased. By tuning these biases properly A star can run faster than Djikstra's without loss of the ability to find the shortest path

    If no hueristic is provided, this algorithm is equivilant to Dijkstra's algorithm.

    usage:
    shortest_path = AStar.find_path(start_node, goal_condition, hueristic=hueristic)

    Warning! - if any of the starting nodes meet the goal condition this will return an empty path.
    """
    # 
    @staticmethod #  
    def find_path(starting_nodes: [Node], goal_condition: GoalCondition, *, hueristic: Hueristic=NullHueristic) -> Path:
        """ #  
        Finds the shortest path from any starting node to a node which meets the goal condition using the A start algorithm.

        starting_nodes - all nodes which the path may start from
        goal_condition - a \'pathfinder.GoalCondition\' which tells us when we have reached our goal
        hueristic - a \'pathfinder.Hueristic\' which biases our distance estimates to make the algorithm run faster.
        """
        # 
        #  declare data structures
        #   stores the places we have seen an edge to and are yet to explore
        unexplored = Heap()
        #   stores all the places we have explored
        explored = set()
        #   stores the optimal edge leading to each node
        incoming_edge: dict[Node, Edge] = dict()
        #   stores the shortest distance to each node
        minimum_distance: dict[Node, float] = dict()
        # 
        #  declare state variables!
        #   records whether we have found a path to our destination
        path_found = False
        #   records the final node of our path to the destination
        path_final_node = None
        # 
        #  retreive problem specific functions
        hueristic = hueristic.hueristic
        is_goal = goal_condition.is_goal
        # 
        #  define exploration function
        def explore(node: Node):
            """ #  
            finds the outgoing edges of a node and adds them to the exploration list
            """
            # 
            #  record that we have explored this node
            explored.add(node)
            # 
            #  deal with reaching our destination!
            if is_goal(node):
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
                    hueristic(edge.destination)
                    ))
            # 
        # 
        #   explore all starting nodes
        for node in starting_nodes:
            incoming_edge[node] = None
            minimum_distance[node] = 0
            explore(node)
        # 
        #  explore nodes until we reach our destination!
        while not (path_found or unexplored.is_empty()):
            #  unpack our exploration vector
            vector = unexplored.pop()
            edge = vector.edge
            source_node = edge.source
            destination_node = edge.destination
            # 
            #  deal with the node already being explored
            if destination_node in explored:
                continue
            # 
            #  record path information about the destination
            incoming_edge[destination_node] = edge
            minimum_distance[destination_node] = edge.cost + minimum_distance[edge.source]
            # 
            #  explore the destination!
            explore(destination_node)
            # 
        # 
        #  construct the optimal path from the information we aquired!
        path = Path()
        current_node = path_final_node
        while incoming_edge[current_node] != None:
            path.append_front_edge(incoming_edge[current_node])
            current_node = incoming_edge[current_node].source
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
    from .finitegraph import parse_edge_list
    print('Starting test (Not Automatic, please visually inspect)')
    edge_list = [
        ['A','B',1],
        ['A','C',1],
        ['A','D',1],
        ['B','D',1],
        ['C','D',1],
        ['C','E',1],
        ['C','F',3],
        ['D','E',2],
        ['D','F',1],
        ['E','F',1],
        ]
    print(f'Parsing edge list: {edge_list}')
    my_graph = parse_edge_list(edge_list)
    class lookforF(GoalCondition):
        @staticmethod
        def is_goal(node):
            if node.node_id == 'F':
                return True
            return False
    starting_node = my_graph.node['A']
    print('Finding shortest path from A to F')
    shortest_path = AStar.find_path([starting_node], lookforF)
    print(f'{shortest_path=}')
# 
