""" #  
The Breadth First Search (BFS) pathfinidng algorithm.

An easy and simple pathfinding algorithm. Equivilant to A-Start with all costs set to 1 with very very slightly better performance.
"""
# 
#  imports!
from collections import deque
from .graphobjects import Node, Path, Edge
from .pathfinder import Pathfinder, GoalCondition, NoPathError
# 
class BFS(Pathfinder): #  
    """ #  
    A wrapper for the Breadth First Search pathfinding algorithm.

    The BFS pathfinding algorithm is a simple pathfinding algorithm which searches outwards from the starting nodes prioritizing the minimum number of edges crossed to reach the destination.

    The BFS algorithm is not guarenteed to find the shortest path.

    example usage:
        path = BFS.find_path(start_node, goal_condition)

    Warning! - if any of the starting nodes meet the goal condition this will return an empty path.
    """
    # 
    @staticmethod
    def find_path(starting_nodes: [Node], goal_condition: GoalCondition) -> Path:
        """ #  
        Finds a path via a breadth first search algorithm.

        Locates a path from a starting node to a node which meets the goal condition.

        starting_nodes - The list of all nodes which the path may start from
        goal_condition - A \'pathfinder.GoalCondition\' which tells us when we have reached our goal

        Warning! - if any of the starting nodes meet the goal condition this will return an empty path.
        """
        # 
        #  declare data structures
            #stores the places we have seen an edge to and are yet to explore
        unexplored: deque[Edge] = deque()
            #stores all the places we have explored
        explored: set[Node] = set()
            #stores the optimal edge leading to each node
        incoming_edge: dict[Node, Edge] = dict()
        # 
        #  declare state variables!
            #records whether we have found a path to our destination
        path_found: bool = False
            #records the final node of our path to the destination
        path_final_node: Node = None
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
                unexplored.append(edge)
            # 
        # 
        def explore_edge(edge: Edge): #  
            #  ignore redundant paths!
            if edge.destination in explored:
                return
            # 
            #  leave a trail of breadcrumbs that we can follow
            incoming_edge[edge.destination] = edge
            # 
            #  explore the node which this edge leads to!
            explore_node(edge.destination)
            # 
        # 
        # 
        #  initialize the values for starting nodes
        for node in starting_nodes:
            incoming_edge[node] = None
        # 
        #  explore the starting nodes!
        for node in starting_nodes:
            explore_node(node)
        # 
        #  explore until we find a path!
        while bool(unexplored) and not path_found:
            edge = unexplored.popleft()
            explore_edge(edge)
        # 
        #  deal with no path existing
        if not path_found:
            raise NoPathError('Pathfinding algorithm found no path from source to destination')
        # 
        #  construct path from edges incoming to each node!
        path = Path()
        current_node = path_final_node
        while incoming_edge[current_node] != None:
            path.append_front_edge(incoming_edge[current_node])
            current_node = incoming_edge[current_node].source
        # 
        return path
# 
#  testing!
if __name__ == '__main__':
    from .test import basic_pathfinder_test
    basic_pathfinder_test(BFS)
    from .test import no_path_pathfinder_test
    no_path_pathfinder_test(BFS)
# 

