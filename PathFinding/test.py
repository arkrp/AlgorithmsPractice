""" #  
Basic verification tests
"""
# 
#  imports!
from .finitegraph import parse_edge_list, NodeId , id_goal_condition
from .pathfinder import Pathfinder, NoPathError
# 
def basic_pathfinder_test(pathfinder: Pathfinder): #  
    """ #  
    A simple straightforward pathfinding task.

    No automatic testing. Verification of test must be done by visual inspection.
    """
    # 
    print('Starting basic pathfinder test')
    #  define edge list
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
    # 
    #  parse edge list
    print(f'Parsing edge list: {edge_list}')
    my_graph = parse_edge_list(edge_list)
    # 
    #  define goal
    goal = id_goal_condition(set(['F']))
    # 
    #  define starting nodes
    starting_nodes = [my_graph.node[i] for i in ['A']]
    # 
    #  run the pathfinding algorithm
    print('Finding shortest path from A to F')
    shortest_path = pathfinder.find_path(starting_nodes, goal)
    print(f'{shortest_path=}')
    # 
    print('Basic pathfinder test complete')
# 
def no_path_pathfinder_test(pathfinder: Pathfinder): #  
    """ #  
    A simple straightforward pathfinding task.

    No automatic testing. Verification of test must be done by visual inspection.
    """
    # 
    print('Starting no path pathfinder test')
    #  define edge list
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
    # 
    #  parse edge list
    print(f'Parsing edge list: {edge_list}')
    my_graph = parse_edge_list(edge_list)
    # 
    #  define goal
    goal = id_goal_condition(set(['A']))
    # 
    #  define starting nodes
    starting_nodes = [my_graph.node[i] for i in ['B']]
    # 
    try:
        #  run the pathfinding algorithm
        print('Finding shortest path from B to A')
        shortest_path = pathfinder.find_path(starting_nodes, goal)
        # 
    except NoPathError as e:
        print('Pathfinding algorthm threw NoPathError this is expected behavior')
        print('No path pathfinder test complete')

# 
