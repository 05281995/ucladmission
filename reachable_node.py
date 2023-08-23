#!/usr/bin/env python3

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    return reachable_internal(adj_list, start_node, set(), set())


def reachable_internal(adj_list, start_node, reachable_nodes, visited_nodes):
    reachable_nodes.update(set(adj_list[start_node]))
    for node in adj_list[start_node]:
        if node not in visited_nodes:
            visited_nodes.add(node)
            reachable_internal(adj_list, node, reachable_nodes, visited_nodes)

    return reachable_nodes

if __name__ == '__main__':
    print(reachable([[1, 3], [2], [0], [4], [3], []], 0))
    print(reachable([[1, 3], [2], [0], [4], [3], []], 3))