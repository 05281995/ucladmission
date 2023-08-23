#!/usr/bin/env python3
""" Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
def mat_to_list (adj_mat):
    adj_list = [] # create output list
    for num_row, row in enumerate(adj_mat):
        adj_list.append([]) # append empty list inside this list for the next step
        for num_elem, elem in enumerate(row):
            if elem == 1:
                adj_list[num_row].append(num_elem)

    return adj_list


if __name__ == '__main__':
    adj_mat = [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]
    print(mat_to_list(adj_mat))