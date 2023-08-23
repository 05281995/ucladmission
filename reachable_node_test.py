#!/usr/bin/env python
import unittest
import reachable_node

class TestReachableNode(unittest.TestCase):
    def test_result(self):
        adj_list = [1, 3], [2], [0], [4], [3], []

        result_start_node_0 = reachable_node.reachable(adj_list, 0)
        self.assertIsInstance(result_start_node_0, set)
        self.assertEqual(result_start_node_0, {0, 1, 2, 3, 4})

        result_start_node_4 = reachable_node.reachable(adj_list, 4)
        self.assertIsInstance(result_start_node_4 , set)
        self.assertEqual(result_start_node_4,{3 , 4})

        result_start_node_5 = reachable_node.reachable(adj_list, 5)
        self.assertIsInstance(result_start_node_5, set )
        self.assertEqual(result_start_node_5, set())


if  __name__ ==  '__main__':
    unittest.main()
